import psutil
import time
import configparser
from utils import send_webhook_alert

# Load config
config = configparser.ConfigParser()
config.read("config.ini")

cpu_threshold = float(config["monitor"]["cpu_threshold"])
interval = int(config["monitor"]["check_interval"])
webhook_url = config["webhook"]["url"]

def monitor_cpu():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f"[INFO] CPU Usage: {cpu_usage}%")
        if cpu_usage > cpu_threshold:
            send_webhook_alert(
                webhook_url,
                alert_type="CPU_OVERLOAD",
                message=f"CPU usage exceeded threshold: {cpu_usage}%",
                value=cpu_usage
            )
        time.sleep(interval)

if __name__ == "__main__":
    print("🚀 AlertHub is running...")
    monitor_cpu()