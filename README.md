
# AI-Based Flood Detection & Road Safety System

![Status](https://img.shields.io/badge/Status-In%20Progress-F4B942?style=flat-square)
![Capstone](https://img.shields.io/badge/Capstone-Team%20Project-7868E6?style=flat-square)

카메라 영상, 수위 센서 및 기상 데이터를 활용하여 터널·지하차도의 침수 위험을 감지하고, 위험 상황에 대응하기 위한 AI 기반 도로 안전 관리 시스템입니다.

영상 분석과 센서 측정값, 외부 강수량 데이터를 종합하여 침수 위험도를 판단하고, 관리자 경고 및 자동 보고서 생성 기능을 구현하는 것을 목표로 합니다.

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![YOLO](https://img.shields.io/badge/YOLO-7868E6?style=flat-square)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)
![LLM](https://img.shields.io/badge/LLM-8B8CFF?style=flat-square)

## My Contributions

### Completed

- **기상청 API 신청 및 호출 테스트**
  - 공공데이터포털에서 API 활용 신청 및 JSON 응답 확인

- **기상청 강수량 데이터 수집 코드 구현**
  - 내성지하차도 및 만덕 진출입로의 위도·경도를 기상청 격자 좌표로 변환
  - 기상청 초단기실황 API를 호출하여 1시간 강수량(RN1) 추출
  - 환경변수를 활용한 API 인증키 관리
  - [📂 Source Code - weather_api.py](./weather_api.py)

- **AI 학습 데이터셋 공동 조사**
  - 침수 감지 모델 학습에 활용할 데이터셋 조사 및 검토

- **시연용 하드웨어 구성 검토 및 구매 목록 정리**
  - Raspberry Pi, 카메라, 수위·빗물 센서 등 하드웨어 구성 검토
  - 야간 촬영 및 방수 구조를 고려한 장비 선정

### Planned

- **시연용 수조 이미지 데이터셋 구축 및 라벨링**
  - 침수 상황별 이미지 수집 및 학습 데이터 구성

- **YOLO 기반 침수 감지 모델 학습 및 최종 모델 완성**
  - 침수 감지 모델 학습, 성능 평가 및 개선

- **Ollama 기반 LLM 자동 보고서 생성 시스템 설계 및 개발**
  - 침수 상황을 설명하는 보고서 생성 기능 구현

- **기상·센서·AI 분석 결과를 활용한 보고서 자동 생성 기능 구현**
  - 다양한 데이터를 통합하여 보고서 생성

- **실제 시연 환경 기반 AI 모델 성능 검증 및 시스템 통합 테스트**
  - 수조 시연 환경에서 감지 정확도 및 시스템 동작 확인

---

## 🏆 Competitions

| Competition | Status |
|---|---|
| 2026 모두의 창업 2차 | 1R 진출 · 참가 중 |
| 교내 콜라보 경진대회 | 참가 중 |
| 교내 캡스톤 경진대회 | 예선 참가 중 |

---

## Repository Information

본 저장소는 캡스톤디자인 팀 프로젝트에서 **직접 담당한 기능의 소스코드와 개발 기록**을 정리하기 위한 개인 저장소입니다.

프로젝트 진행에 따라 구현 코드 및 개발 내용을 지속적으로 업데이트할 예정입니다.
