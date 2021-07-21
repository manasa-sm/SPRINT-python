import schedule
import time
from plyer import notification
def job():
    notification.notify(title="Drink Water", message="Time to drink water and stay hydrated", timeout=10)

schedule.every().hour.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
