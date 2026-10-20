from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse  # 新增这个
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

words = [
    {"word": "abandon", "meaning": "v. 放弃，抛弃"},
    {"word": "benefit", "meaning": "n. 益处 v. 有益于"},
    {"word": "crucial", "meaning": "adj. 至关重要的"},
    {"word": "deteriorate", "meaning": "v. 恶化，退化"},
    {"word": "evaluate", "meaning": "v. 评估，评价"},
    {"word": "fundamental", "meaning": "adj. 基础的，根本的"},
    {"word": "generate", "meaning": "v. 产生，引起"},
    {"word": "hypothesis", "meaning": "n. 假设，假说"},
    {"word": "illustrate", "meaning": "v. 说明，图解"},
    {"word": "justify", "meaning": "v. 证明...是正当的"},
    {"word": "legitimate", "meaning": "adj. 合法的，合理的"},
    {"word": "magnify", "meaning": "v. 放大，夸大"},
    {"word": "neglect", "meaning": "v. 忽视，忽略"},
    {"word": "obscure", "meaning": "adj. 模糊的 v. 使模糊"},
    {"word": "participate", "meaning": "v. 参与，参加"},
    {"word": "qualify", "meaning": "v. 取得资格，使合格"},
    {"word": "reinforce", "meaning": "v. 加强，巩固"},
    {"word": "sustain", "meaning": "v. 维持，支撑"},
    {"word": "transmit", "meaning": "v. 传输，传播"},
    {"word": "vulnerable", "meaning": "adj. 易受伤害的，脆弱的"}
]

# 新增这个根路由，当用户访问网站首页时，把网页文件发给他
@app.get("/")
def read_root():
    return FileResponse("index.html")

@app.get("/api/get_word")
def get_word():
    return random.choice(words)