# AlertHub_Project

**AlertHub**는 로컬 시스템의 주요 자원(CPU, 메모리, 디스크, 네트워크 등)을 지속적으로 모니터링하고, 설정한 임계치를 초과하는 이벤트가 발생할 경우 사용자 정의 Webhook을 통해 실시간 알림을 전송하는 Python 기반의 경량 모니터링 도구입니다.


## 📌 주요 기능

- CPU, 메모리, 디스크, 네트워크 사용량 실시간 모니터링
- 사용자 정의 임계치 설정 및 이벤트 감지
- Webhook을 통한 실시간 알림 전송
- 경량화된 구조로 리소스 부담 최소화
- 간단한 설정 파일(config.ini) 기반 구성


## 🛠️ 설치 및 실행 방법

### 1. 프로젝트 클론

```bash
git clone https://github.com/bigjunhyeok/AlertHub_Project.git
cd AlertHub_Project
```

### 2. 의존성 설치

```bash
pip install -r requirements.txt
```

### 3. 설정 파일 구성

`config.ini` 파일을 열어 모니터링할 자원과 임계치, Webhook URL 등을 설정합니다.

```ini
[CPU]
threshold = 80

[Memory]
threshold = 70

[Disk]
threshold = 90

[Network]
threshold = 1000

[Webhook]
url = https://your-webhook-url.com
```

### 4. 모니터링 시작

```bash
python main.py
```


## 🧩 주요 파일 설명

- `main.py` : 모니터링 로직의 진입점으로, 설정 파일을 읽고 모니터링을 시작합니다.
- `utils.py` : 시스템 자원 상태를 확인하고, 임계치 초과 여부를 판단하는 유틸리티 함수들을 포함합니다.
- `config.ini` : 모니터링 대상 자원, 임계치, Webhook URL 등을 설정하는 파일입니다.

## 📄 예시

임계치를 초과하는 경우, 설정한 Webhook URL로 다음과 같은 JSON 형식의 알림이 전송됩니다:

```json
{
  "resource": "CPU",
  "usage": 85,
  "threshold": 80,
  "timestamp": "2025-05-12T13:34:41+09:00"
}
```


## 🧪 테스트 및 개발 환경

- Python 3.8 이상
- 테스트 환경: Windows 10, Ubuntu 20.04
- 의존성: `psutil`, `requests` 등