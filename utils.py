import requests
import datetime

def send_webhook_alert(webhook_url, alert_type, message, value):
    """
    지정된 webhook_url로 JSON 알림 메시지를 전송합니다.

    :param webhook_url: Webhook 수신 URL
    :param alert_type: 알림 종류 (예: "CPU_OVERLOAD")
    :param message: 알림 메시지 내용
    :param value: 측정된 값 (예: CPU 사용률)
    """
    payload = {
        "type": alert_type,
        "message": message,
        "value": value,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=5)
        response.raise_for_status()
        print(f"[ALERT SENT] {payload}")
    except requests.exceptions.RequestException as e:
        print(f"[ERROR] Failed to send webhook: {e}")


def db_handler():
    return None