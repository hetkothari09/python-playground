import uvicorn
from fastapi import FastAPI, Body, File, Request, UploadFile, Cookie, Header
from pydantic import BaseModel, Field
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import shutil
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.gzip import GZipMiddleware
from typing_extensions import Optional
import time

# Async functions can wait for operations to complete such as fetching, inserting etc.

app = FastAPI()
templates = Jinja2Templates(directory="templates")


class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        print(f"Incoming request: {request.method} {request.url}")
        response = await call_next(request)
        response_time = time.time() - start_time
        response.headers["X_response_time"] = str(response_time)
        print(f"Response status is: {response.status_code}")
        print(f"Total processing time was: {response_time:.2f}")
        return response

app.add_middleware(CustomMiddleware)

@app.get('/hisay')
async def hisay():
    return {"message": "Hello"}








'''
CORS implementation
Basically when you want to allow sharing of resources between different network origin, then you have
to specify the origins using CORS.
Example if a frontend is running on localhost:5000 and backend is running on localhost:8000, then
without using CORS you wont be able to share resources and will get an error
'''

# allowed_origins = [
#     "http://localhost:8000",
#     "http://localhost:5000",
#     "https://localhost:5000"
# ]
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins = allowed_origins,
#     allow_credentials = True,
#     allow_method = ["*"],
#     allow_headers = ["*"]
# )


@app.get('/')
async def index():
    return {"message": "Hey there!"}

@app.get('/bye')
async def bye():
    return {"message": "BYEE!"}

@app.get('/hello/{name}')
async def say_hello(name:str):
    return {"message": f"Hello {name}"}

@app.get('/hello/{name}/{age}')
async def say_hello_age(name: str, age: int):
    return {"message": f"Hello {name} with {age} years old"}

class Student(BaseModel):
    id: int | None
    name: str
    # age: int

# @app.post('/students/')
# async def validate_student(s1: Student):
#     return s1

'''
Body(...) takes the values from the response body (...) indicates it as a compulsion
'''
@app.post('/students')
async def get_body_values(name:str=Body(...), age:int=Body(...)):
    return {"name": name, "age": age}

'''
Use HTMLResponse to generate the response in html format
'''
@app.get('/html')
async def render_html():
    ret = '''
        <html>
        <body>
            <h1> Hey </h1>
        </body>
        </html>
    '''
    return HTMLResponse(content=ret)

'''
Query parameters
eg: http://127.0.0.1:8000/hello?name=het&age=21
'''
@app.get('/hello')
async def say_hi(name:str, age:int):
    return {"message": f"Hello {name} and you are {age} years old"}


'''
Multiple types of parameters
college - path parameter
age - query parameter
student - validating using pydantic Student class 
model_dump - is basically dict
'''
@app.post('/students_new/{college}')
async def multiple_params(college:str, age:int, student:Student):
    result = {"college": college, "age": age, **student.model_dump()}
    return result


'''
File transfer using FastAPI
use: jinja2(templates)
shutil - used for high level file operations
UploadFile
'''
@app.get('/upload', response_class=HTMLResponse)
async def upload_file(request: Request):
    return templates.TemplateResponse('upload.html', {"request": request})

@app.post('/uploader')
async def create_upload_file(file: UploadFile = File(...)):
    with open('destination.png', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}

'''
Creating and reading Cookies
'''
@app.get('/cookie')
async def create_cookie():
    response = {"message": "Cookie created"}
    result = JSONResponse(content=response)
    result.set_cookie(key="username", value="admin")
    result.set_cookie(key="pwd", value="root")
    return result

@app.get('/read_cookie')
async def read_cookie(username: str = Cookie(None), pwd: str = Cookie(None)):
    return {"username": username, "pwd": pwd}


'''
Header parameters
'''
@app.get('/headers')
async def read_header(accept_language: Optional[str] = Header(None)):
    return {"Accept Language": accept_language}


'''
Response Model
Basically it allows us to decide which model you want to use in the response.
Basically here i have used both NewStudent as well as Percent model, but for response i have used Percent model
'''
class NewStudent(BaseModel):
    name: str
    marks: int
    percent_marks: float

class Percent(BaseModel):
    name:str
    percent_marks: float

@app.post('/marks', response_model=Percent)
async def get_marks(s1: NewStudent):
    s1.percent_marks = (s1.marks/2)
    return s1

'''
Compression of files using GZipMiddleware.
'''

# app.add_middleware(GZipMiddleware, minimum_size=1000)

@app.get('/largefile')
async def gzip_file():
    data = "x" * 2000
    return data


if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, reload=True)
