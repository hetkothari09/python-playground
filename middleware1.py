from fastapi import FastAPI, Request
from sqlalchemy.orm import defer
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

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
