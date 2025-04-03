from celery import Celery
from celery.schedules import crontab


'''
Celery is used to schedule tasks in a queue
it is basically used to run background tasks like email sending, report generation, api data fetching etc without interrupting
main process

Celery beat is used to schedule tasks periodically
We can schedule the tasks when to occur using crontab
'''


app = Celery(
    "celery_beat1",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0"
)

@app.task
def send_reminder():
    print("Reminder to drink water!")

app.conf.beat_schedule = {
    "send_reminder_per_minute": {
        "task": "celery_beat1.send_reminder",
        "schedule": crontab(minute="*/1"),
    },
}

