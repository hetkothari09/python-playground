from fastapi import FastAPI
import os
from fastapi.responses import FileResponse

app = FastAPI()

@app.get('/download')
async def download_file():
    file_name = 'AAPL.csv'
    if os.path.exists(file_name):
        return FileResponse(file_name, filename='downloaded_file.csv', media_type='application/pdf')
    else:
        return {"File not Found!"}