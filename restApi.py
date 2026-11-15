from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Simple REST API", version="1.0")

# 요청 데이터 검증을 위한 Pydantic 모델
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# 임시 데이터베이스 역할의 리스트
items_db = []

@app.get("/")
def read_root():
    return {"message": "FastAPI 서버가 정상적으로 실행 중이야!"}

@app.get("/items")
def get_items():
    return {"items": items_db}

@app.post("/items")
def create_item(item: Item):
    items_db.append(item)
    return {"message": "아이템이 성공적으로 등록되었어!", "item": item}