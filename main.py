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
database.import_words_from_json()
database.init_checkin_db()

#返回index.html网页
@app.get("/")
def read_root():
    return FileResponse("index.html")

#去数据库拿随机单词
@app.get("/api/get_word")
def get_word():
    return database.get_random_word()

# 接受打卡请求。这个就是前台接客的柜台！必须写在 main.py 里！
@app.post("/api/checkin")
def do_checkin():
    database.add_checkin()
    return {"message": "打卡成功！今天你超棒！"}