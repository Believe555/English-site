from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import database

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# 启动时初始化两个表
database.init_db()
database.init_checkin_db()

@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/api/get_word")
def get_word():
    return database.get_random_word()

# 这个就是前台接客的柜台！必须写在 main.py 里！
@app.post("/api/checkin")
def do_checkin():
    database.add_checkin()
    return {"message": "打卡成功！今天你超棒！"}