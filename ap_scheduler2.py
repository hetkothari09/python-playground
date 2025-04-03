from asyncio import sleep

from apscheduler.schedulers.background import BackgroundScheduler
import time
from datetime import datetime


def interval_task():
    print(f"Task executed at {datetime.now()}")


scheduler = BackgroundScheduler()
scheduler.add_job(interval_task, 'interval', seconds=10)

scheduler.start()

while True:
    time.sleep(1)