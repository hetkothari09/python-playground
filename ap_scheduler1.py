from apscheduler.schedulers.background import BackgroundScheduler
import time

'''
APScheduler helps us to run python tasks on a particular time or in particular time intervals.
We can schedule our code to run at a specific time. 
It can be either once or periodically.
'''


def task_run():
    print(f"Task executed at {time.time()}")

scheduler = BackgroundScheduler()
scheduler.add_job(task_run, 'date', run_date='2025-04-02 15:32:30')
scheduler.start()

while True:
    time.sleep(1)