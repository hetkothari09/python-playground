from celery_app import add

result = add.delay(4, 6)

print(f"The result fetched by celery: {result.get()}")
