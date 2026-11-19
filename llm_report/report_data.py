
import json

# 1. 현재 침수 관측 데이터
report_data = {
    "location": "내성지하차도",
    "timestamp": "2026-11-19 18:00:00",
    "water_level": "경고",
    "rainfall": 35.0
}

# 2. 수위 단계 이력
water_level_history = [
    {
        "timestamp": "2026-11-19 17:00:00",
        "water_level": "정상"
    },
    {
        "timestamp": "2026-11-19 17:20:00",
        "water_level": "주의"
    },
    {
        "timestamp": "2026-11-19 17:40:00",
        "water_level": "경고"
    },
    {
        "timestamp": "2026-11-19 18:00:00",
        "water_level": "경고"
    }
]

# 3. AI 영상 분석 결과
ai_result = {
    "model": "YOLO",
    "flood_detected": True,
    "confidence": 0.95,
    "water_level": "경고"
}

# 4. 경보 발생 이력
alert_history = [
    {
        "timestamp": "2026-11-19 17:20:00",
        "alert_level": "주의",
        "message": "침수 주의 단계 진입"
    },
    {
        "timestamp": "2026-11-19 17:40:00",
        "alert_level": "경고",
        "message": "침수 경고 단계 진입"
    }
]

# 5. 전체 보고서 입력 데이터 통합
report_data["water_level_history"] = water_level_history
report_data["ai_result"] = ai_result
report_data["alert_history"] = alert_history

# 6. Python 딕셔너리를 JSON 문자열로 변환
report_json = json.dumps(
    report_data,
    ensure_ascii=False,
    indent=4
)

# 7. 단독 실행 시 JSON 출력
if __name__ == "__main__":
    print(report_json)
