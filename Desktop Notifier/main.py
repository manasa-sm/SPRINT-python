import time
from plyer import notification
notification.notify(
        title="BlueLearn Python Sprint",
        message="This is a Desktop Notification",
        timeout=2
    )
time.sleep(7)
