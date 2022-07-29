
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
import os

app=FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True , allow_methods=["*"], allow_headers=["*"])

@app.post("/message")
def message(upload_file: UploadFile =File(...)):
    print("writing file")
    # src_file_path=create_file(upload_file.filename)
    src_file_path = f'{os.getcwd()}/file_folder/{upload_file.filename}'
    with open(src_file_path , 'wb+') as input_file:
        content=upload_file.file.read()
        input_file.write(content)
        

    return upload_file.filename;
