from fastapi import FastAPI, Depends
from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from typing import Optional
from pydantic import BaseModel, EmailStr
from requests import HTTPError

app = FastAPI()

SECRET_KEY = '7014ea47e74396287c8c263c3686e982'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth_lib = OAuth2PasswordBearer("token")

dummy_data = {
    "het": {
        "name": "het",
        "hashed_password": pwd_context.hash("pass123"),
        "email": "het@gmail.com",
        "disabled": False
    }
}


class User(BaseModel):
    name: str
    email: Optional[EmailStr]
    disabled: Optional[bool]

class Token(BaseModel):
    access_token: str
    token_type: str


def create_access_token(data: dict, expire_delta: timedelta):
    token_data = data.copy()
    expire_time = datetime.now() + expire_delta
    token_data.update({"exp": expire_time})

    return jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(username: str, password: str):
    user = dummy_data.get(username)

    if not user:
        return False
    if not pwd_context.verify(password, user["hashed_password"]):
        return False

    return user

def get_current_user(token: str = Depends(oauth_lib)):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    username: str = payload.get('sub')
    if username is None:
        raise JWTError("Invalid Token")

    user = dummy_data.get(username)
    if user is None:
        raise JWTError("User does not exist!")

    return User(**user)

@app.post('/token', response_model=Token)
def user_login_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)

    if user is None:
        raise JWTError("Invalid Creds")

    expire_token_time = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = create_access_token(
        data = {'sub': form_data.username},
        expire_delta = expire_token_time
    )

    return {"access_token": access_token, "token_type": "bearer"}

@app.get('/user/me')
async def current_user_validate(current_user: User = Depends(get_current_user)):
    return current_user