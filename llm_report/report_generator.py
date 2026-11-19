
import requests
import time
import json
from report_data import report_json


# 1. Ollama API 설정
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen3:1.7b"


# 2. Python 기반 사실 정보 작성
def create_fact_report(data):

    report = []

    # 관측 개요
    report.append("## 1. 관측 개요 및 현재 현황")
    report.append(f"- 관측 위치: {data['location']}")
    report.append(f"- 관측 시간: {data['timestamp']}")
    report.append(f"- 현재 수위 단계: {data['water_level']}")
    report.append(f"- 시간당 강수량: {data['rainfall']}mm/h")

    # 수위 단계 변화 이력
    report.append("\n## 2. 수위 단계 변화 이력")

    for record in data["water_level_history"]:
        report.append(
            f"- {record['timestamp']} : "
            f"{record['water_level']}"
        )

    # AI 영상 분석 결과
    ai = data["ai_result"]

    report.append("\n## 3. AI 영상 분석 결과")
    report.append(f"- 분석 모델: {ai['model']}")
    report.append(f"- 수위 단계: {ai['water_level']}")

    detected = "감지됨" if ai["flood_detected"] else "미감지"

    report.append(f"- 침수 징후: {detected}")
    report.append(f"- 분석 신뢰도: {ai['confidence'] * 100:.1f}%")

    # 경보 발생 이력
    report.append("\n## 4. 경보 발생 이력")

    if data["alert_history"]:
        for alert in data["alert_history"]:
            report.append(
                f"- {alert['timestamp']} : "
                f"{alert['message']}"
            )
    else:
        report.append("- 경보 발생 이력 없음")

    return "\n".join(report)


# 3. LLM 분석용 프롬프트 구성
def create_prompt(data):

    prompt = f"""
당신은 도로 침수 안전 관리 시스템의 분석 담당자입니다.

아래 관측 데이터를 참고하여 한국어로 작성하세요.

[작성 규칙]
1. 제공된 데이터만 근거로 분석하세요.
2. 확인되지 않은 사실을 추측하지 마세요.
3. 수위 단계 유지가 실제 수위 상승을 의미하지는 않습니다.
4. 대응 권고와 실제 시행된 조치를 구분하세요.
5. 관측 수치와 이력을 불필요하게 반복하지 마세요.
6. 각 항목은 1~2문장으로 작성하세요.
7. 전체 내용은 250자 이내로 작성하세요.
8. 실제 대응은 관리자가 정해진 안전관리 기준에 따라
   결정하도록 권고하세요.

[출력 형식]
## 5. 상황 종합 분석
분석 내용

## 6. 관리자 대응 권고
권고 내용

[관측 데이터]
{data}
"""
    return prompt


# 4. Ollama 기반 상황 분석 생성
def generate_analysis(data):

    payload = {
        "model": MODEL_NAME,
        "prompt": create_prompt(data),
        "stream": False,
        "think": False,
        "keep_alive": "30m",
        "options": {
            "temperature": 0.1,
            "num_predict": 384
        }
    }

    try:

        response = requests.post(
            OLLAMA_URL,
            json=payload,
            timeout=300
        )

        response.raise_for_status()

        result = response.json()

        # 출력 잘림 검사
        if result.get("done_reason") == "length":
            return {
                "success": False,
                "error": "토큰 제한으로 분석이 중단되었습니다."
            }

        # 생성 완료 검사
        if not result.get("done"):
            return {
                "success": False,
                "error": "분석이 정상적으로 완료되지 않았습니다."
            }

        analysis = result["response"].strip()

        if not analysis:
            return {
                "success": False,
                "error": "생성된 분석 내용이 없습니다."
            }

        return {
            "success": True,
            "analysis": analysis
        }

    except requests.exceptions.ConnectionError:
        return {
            "success": False,
            "error": "Ollama 서버에 연결할 수 없습니다."
        }

    except requests.exceptions.Timeout:
        return {
            "success": False,
            "error": "분석 생성 시간이 초과되었습니다."
        }

    except (
        requests.exceptions.RequestException,
        ValueError,
        KeyError,
        TypeError
    ) as e:
        return {
            "success": False,
            "error": str(e)
        }


# 5. Python 보고서와 LLM 분석 결과 통합
def generate_report(data):

    try:

        # JSON 문자열을 Python 딕셔너리로 변환
        parsed_data = json.loads(data)

        # Python 기반 사실 정보 생성
        fact_report = create_fact_report(parsed_data)

    except (ValueError, KeyError, TypeError, AttributeError) as e:
        return {
            "success": False,
            "error": f"입력 데이터 오류: {e}"
        }

    # LLM 기반 상황 분석 생성
    result = generate_analysis(data)

    if not result["success"]:
        return {
            "success": False,
            "error": result["error"],
            "partial_report": fact_report
        }

    # 최종 보고서 결합
    final_report = (
        "# 침수 상황 보고서\n\n"
        + fact_report
        + "\n\n"
        + result["analysis"]
    )

    return {
        "success": True,
        "model": MODEL_NAME,
        "report": final_report
    }


# 6. 단독 실행 테스트
if __name__ == "__main__":

    print("침수 상황 보고서 생성 중...\n")

    start_time = time.perf_counter()

    result = generate_report(report_json)

    end_time = time.perf_counter()

    print(
        f"보고서 생성 소요 시간: "
        f"{end_time - start_time:.2f}초"
    )

    if result["success"]:

        print("=" * 50)
        print("침수 상황 자동 생성 보고서")
        print("=" * 50)

        print(result["report"])

    else:

        print("보고서 생성 실패")
        print(result["error"])

        if "partial_report" in result:
            print("\n[확인 가능한 관측 정보]")
            print(result["partial_report"])
