from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

for jobs in scheduler.get_jobs():
    print(jobs)