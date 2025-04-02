import uvicorn
from fastapi import FastAPI

app = FastAPI()

# Async functions can wait for operations to complete such as fetching, inserting etc.

@app.get('/')
async def index():
    return {"message": "Hey there!"}

@app.get('/bye')
async def bye():
    return {"message": "BYEE!"}

@app.post('/hello/{name}')
async def say_hello(name:str):
    return {"message": f"Hello {name}"}

@app.post('/hello/{name}/{age}')
async def say_hello_age(name: str, age: int):
    return {"message": f"Hello {name} with {age} years old"}

# if __name__ == '__main__':
#     uvicorn.run("fastapi1:app", host='127.0.0.1', port=8000, reload=True)