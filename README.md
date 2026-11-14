
# AI-Based Flood Detection & Road Safety System

> **AI 기반 지능형 침수 감지 및 도로 안전 관리 시스템**

![Status](https://img.shields.io/badge/Status-In%20Progress-F4B942?style=flat-square)
![Capstone](https://img.shields.io/badge/Capstone-Team%20Project-7868E6?style=flat-square)
![Team](https://img.shields.io/badge/Team-return%200%3B-4479A1?style=flat-square)

## 01. Project Overview

### 프로젝트 소개

본 프로젝트는 터널 및 지하차도에서 발생할 수 있는 침수 상황을 조기에 감지하고, 위험 상황에 신속하게 대응하기 위한 **AI 기반 지능형 침수 감지 및 도로 안전 관리 시스템**입니다.

카메라 영상 분석, 수위 센서, 강수량 등 다양한 데이터를 결합하여 침수 위험도를 판단하고, 관리자에게 경고 정보를 제공하는 것을 목표로 합니다.

단일 센서의 측정 결과에만 의존하지 않고, **영상 분석과 센서 데이터 및 외부 기상정보를 함께 활용하여 침수 상황을 종합적으로 판단**하도록 설계하고 있습니다.

### 개발 배경

집중호우로 인해 터널과 지하차도에 침수가 발생할 경우, 차량 운전자가 위험을 인지하지 못한 채 진입하면 인명피해로 이어질 수 있습니다.

따라서 침수 상황을 실시간으로 감지하고, 위험도를 판단하여 신속하게 경고할 수 있는 시스템이 필요하다고 생각했습니다.

본 프로젝트에서는 AI 영상 분석과 다양한 환경 데이터를 활용하여 침수 감지의 신뢰성을 높이고, 관리자 중심의 통합 모니터링 환경을 구현하고자 합니다.

### 프로젝트 목표

- 카메라 영상을 활용한 침수 상황 감지
- 수위 센서를 활용한 수위 변화 측정
- 기상청 API를 활용한 외부 강수량 데이터 수집
- 영상·센서·기상 데이터를 결합한 침수 위험도 판단
- 위험 상황 발생 시 자동 경고 및 차량 진입 차단 권고
- 관리자 대시보드를 통한 실시간 상태 확인
- LLM을 활용한 침수 상황 보고서 자동 생성

---

## 02. System Architecture

### 시스템 동작 흐름

```text
[환경 데이터 수집]
 ├── 카메라 영상
 ├── 수위 센서
 ├── 빗물 센서
 └── 기상청 API
          |
          v
[데이터 처리 및 분석]
 ├── YOLO 기반 영상 분석
 ├── 센서 데이터 처리
 └── 강수량 데이터 수집
          |
          v
[침수 위험도 판단]
          |
          v
[위험 상황 대응]
 ├── 관리자 경고
 └── 차량 진입 차단 권고
          |
          v
[관리자 대시보드]
          |
          v
[LLM 기반 보고서 자동 생성]
```

※ 위 구성은 프로젝트의 목표 아키텍처이며, 일부 기능은 개발 예정입니다.

### 주요 구성 요소

| 구성 요소 | 역할 |
|---|---|
| Raspberry Pi | 센서 및 카메라 연동 |
| Camera | 침수 상황 영상 수집 |
| Water Level Sensor | 수위 변화 측정 |
| Rain Sensor | 강우 감지 |
| Weather API | 외부 강수량 데이터 수집 |
| YOLO | 침수 관련 영상 분석 |
| Spring Boot | 백엔드 API 및 데이터 처리 |
| MySQL | 수집 데이터 저장 및 관리 |
| Dashboard | 관리자 모니터링 |
| Ollama / LLM | 침수 상황 보고서 자동 생성 |

---

## 03. Tech Stack

### Language & Framework

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)

### AI & Data

![YOLO](https://img.shields.io/badge/YOLO-7868E6?style=flat-square)
![LLM](https://img.shields.io/badge/LLM-8B8CFF?style=flat-square)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=flat-square&logo=mysql&logoColor=white)

### Hardware

![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-A22846?style=flat-square&logo=raspberrypi&logoColor=white)

### External API & Libraries

- 기상청 초단기실황 조회 API
- Requests
- pyproj
- python-dotenv

※ 기술 스택에는 현재 사용 중인 기술과 향후 개발에 사용할 예정인 기술이 함께 포함되어 있습니다.

---

## 04. My Contributions

본 저장소는 팀 프로젝트 전체 소스코드가 아닌, **프로젝트에서 직접 담당한 기능과 개인 개발 기록을 정리하기 위한 저장소**입니다.

### Completed

#### 1. 기상청 API 신청 및 호출 테스트

- 공공데이터포털에서 기상청 단기예보 조회서비스 활용 신청
- API 인증키 발급 및 요청 테스트
- HTTP GET 요청 및 JSON 응답 구조 분석
- 환경변수를 활용한 API 인증키 관리

#### 2. 기상청 강수량 데이터 수집 기능 구현

**담당 기능:** 두 관측 지점의 위도·경도를 기상청 격자 좌표로 변환하고, 강수량 데이터를 조회하는 Python 프로그램 개발

**관측 지점**

| 관측 지점 | 위도(lat) | 경도(lon) |
|---|---|---|
| 내성지하차도 | 35.2059 | 129.0832 |
| 만덕 진출입로 | 35.2125 | 129.0385 |

**구현 내용**

- 관측 지점별 위도·경도 정보 관리
- Lambert Conformal Conic 투영을 활용한 좌표 변환
- 기상청 API 요청을 위한 격자 좌표 계산
- 관측 기준 날짜 및 시간 계산
- Requests 라이브러리를 활용한 HTTP GET 요청
- JSON 응답 데이터 파싱
- `RN1` 항목을 이용한 1시간 강수량 추출
- 두 지점의 강수량 조회 및 출력

**구현 과정**

```text
관측 지점 선택
      |
      v
위도·경도 조회
      |
      v
기상청 격자 좌표 변환
      |
      v
관측 기준 날짜·시간 계산
      |
      v
기상청 API 요청
      |
      v
JSON 응답 파싱
      |
      v
RN1(1시간 강수량) 추출
      |
      v
강수량 출력
```

**구현 결과**

두 관측 지점에 대해 API 요청 및 강수량 데이터 추출이 정상적으로 이루어지는 것을 확인했습니다.

**Source Code**

[weather_api.py 바로가기](./weather/weather_api.py)

#### 3. AI 학습 데이터셋 공동 조사

- 침수 감지 AI 모델 학습에 활용할 데이터셋 조사
- 프로젝트 목적에 적합한 영상 데이터 활용 가능성 검토
- 팀원들과 데이터셋 구성 방향 논의

#### 4. 시연용 하드웨어 구성 검토 및 구매 목록 정리

- Raspberry Pi 기반 센서 및 카메라 구성 검토
- 수위 센서 및 빗물 센서 활용 방안 논의
- 야간 촬영을 고려한 카메라 구성 검토
- 방수 및 하드웨어 설치 방식 검토
- 시연 환경에 필요한 장비 목록 정리

---

### Planned

#### 1. 시연용 수조 이미지 데이터셋 구축 및 라벨링

- 시연 환경에서 사용할 이미지 데이터 수집
- 침수 상황별 이미지 데이터셋 구성
- AI 학습에 필요한 데이터 라벨링
- 학습·검증 데이터셋 분리 및 정리

#### 2. YOLO 기반 침수 감지 모델 개발

- YOLO 모델 학습 환경 구축
- 침수 상황 감지를 위한 모델 학습
- 학습 결과 분석 및 모델 개선
- 최종 침수 감지 모델 완성

#### 3. Ollama 기반 LLM 자동 보고서 생성 시스템 개발

- Ollama 기반 LLM 실행 환경 구성
- 침수 상황 보고서 구조 설계
- 보고서 자동 생성 기능 구현
- 생성 결과 검토 및 개선

#### 4. 기상·센서·AI 분석 결과를 활용한 보고서 생성

- 기상청 강수량 데이터 활용
- 수위 센서 측정값 활용
- AI 영상 분석 결과 활용
- 통합 데이터를 기반으로 침수 상황 보고서 생성

#### 5. AI 모델 성능 검증 및 시스템 통합 테스트

- 실제 시연 환경에서 AI 모델 동작 검증
- 침수 상황별 감지 결과 확인
- 센서·기상·AI 데이터 연동 테스트
- 전체 시스템 통합 동작 확인

---

## 05. Implementation Details

### Weather Data Collection

**기상청 API 기반 강수량 데이터 수집**

본 기능은 외부 기상정보를 침수 위험도 판단에 활용하기 위해 개발했습니다.

기상청 API는 위도·경도 대신 격자 좌표를 요청 파라미터로 사용하므로, 관측 지점의 좌표를 기상청 격자 좌표로 변환하는 과정이 필요했습니다.

이를 위해 Python의 `pyproj` 라이브러리를 활용하여 좌표 변환 기능을 구현했습니다.

또한 기상청 초단기실황 API를 호출하고, 반환된 JSON 데이터에서 1시간 강수량을 나타내는 `RN1` 항목을 추출하도록 구현했습니다.

API 인증키는 소스코드에 직접 작성하지 않고 환경변수로 관리했습니다.

### 사용 기술

| 기술 | 활용 목적 |
|---|---|
| Python | 강수량 수집 프로그램 구현 |
| pyproj | 위도·경도 좌표 변환 |
| Requests | HTTP GET 요청 |
| python-dotenv | 환경변수 로드 |
| datetime | 관측 기준 날짜 및 시간 계산 |
| JSON | API 응답 데이터 처리 |

### 개발 과정에서 학습한 내용

- API와 REST API의 기본 개념
- HTTP GET 요청과 쿼리 파라미터
- API Key와 환경변수 관리
- JSON 데이터 구조 및 파싱
- Python 딕셔너리와 리스트
- 중첩 반복문을 활용한 데이터 탐색
- 기상청 격자 좌표 변환 원리

---

## 06. Project Structure

```text
AI-Flood-Detection-System/
├── weather/
│   └── weather_api.py
├── .gitignore
└── README.md
```

본 저장소는 개인 기여 코드 중심으로 구성되며, 향후 직접 구현한 기능을 추가할 예정입니다.

---

## 07. Competitions

본 프로젝트는 캡스톤디자인 과제로 진행하는 동시에 교내외 경진대회에도 참여하고 있습니다.

| Competition | Status |
|---|---|
| 2026 모두의 창업 2차 | 1R 진출 · 참가 중 |
| 교내 콜라보 경진대회 | 참가 중 |
| 교내 캡스톤 경진대회 | 예선 참가 중 |

### 2026 모두의 창업 2차

**Status:** 1R 진출 · 참가 중

AI 기반 침수 감지 및 도로 안전 관리 시스템을 바탕으로 참가하고 있습니다.

현재 1라운드에 진출한 상태이며, 이후 진행 결과에 따라 내용을 업데이트할 예정입니다.

### 교내 콜라보 경진대회

**Status:** 참가 중

캡스톤 프로젝트를 기반으로 참가 중인 교내 경진대회입니다.

향후 진행 과정과 결과를 추가할 예정입니다.

### 교내 캡스톤 경진대회

**Status:** 예선 참가 중

캡스톤디자인 프로젝트의 개발 내용과 결과를 바탕으로 참가하고 있습니다.

현재 예선 참가 단계이며, 추후 결과를 업데이트할 예정입니다.

---

## 08. Development Progress

| Task | Status |
|---|---|
| 기상청 API 신청 및 호출 테스트 | Completed |
| 강수량 데이터 수집 코드 구현 | Completed |
| AI 학습 데이터셋 공동 조사 | Completed |
| 하드웨어 구성 검토 및 구매 목록 정리 | Completed |
| 시연용 이미지 데이터셋 구축 및 라벨링 | Planned |
| YOLO 침수 감지 모델 개발 | Planned |
| Ollama 기반 보고서 생성 기능 개발 | Planned |
| 기상·센서·AI 통합 보고서 생성 | Planned |
| AI 모델 성능 검증 및 시스템 통합 테스트 | Planned |

---

## 09. Future Improvements

향후 개발 과정에서 다음 사항을 검토하고 개선할 예정입니다.

- 기상청 API 요청 실패 및 응답 오류 처리
- 강수량 데이터 수집 기능의 안정성 개선
- AI 영상 분석 결과와 센서 데이터 연동
- 침수 위험도 판단 정확도 개선
- LLM 기반 자동 보고서 생성 기능 고도화
- 시연 환경 기반 통합 테스트 및 성능 평가

---

## 10. Development Notes

본 프로젝트를 진행하며 학습한 내용과 구현 과정은 기술 블로그에도 정리하고 있습니다.

- [Velog](https://velog.io/)

※ 상세 게시글 링크는 추후 추가 예정입니다.

---

**This repository documents my personal contributions to an ongoing capstone team project.**
