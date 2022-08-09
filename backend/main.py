from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware 
import os,sys
from word2txt.word2txt_converter import convert_docx2txt

app=FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True , allow_methods=["*"], allow_headers=["*"])

# sys.path.append('C:\\Web Development Folder New\\Heroku_fastapi\\heroku\\heroku\\backend')

print(sys.path)

@app.post("/message")
def message(upload_file: UploadFile =File(...)):
    print("writing file")
    # src_file_path=create_file(upload_file.filename)
    src_file_path = f".\\file_folder\\sample.docx"
    # src_file_path = f"file_folder/{upload_file.filename}"
    with open(src_file_path , 'wb+') as input_file:
        content=upload_file.file.read()
        input_file.write(content)

    dest_file_path = f'.\\file_folder\\Myfile.txt'

    convert_docx2txt(src_file_path,dest_file_path);
    

    return upload_file.filename;

# 'C:\\Web Development Folder New\\Heroku_fastapi\\heroku\\heroku\\backend', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin

# ['.', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\Scripts\\uvicorn.exe', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
# 'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310',
#  'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages', 
#  'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32', 
#  'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\win32\\lib', 
#  'C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\Pythonwin']