FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

#RUN #uvicorn jwt_authentication_prac:app --reload

EXPOSE 8000

CMD ["uvicorn", "jwt_authentication_prac:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
