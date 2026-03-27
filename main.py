
import os

from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client, Client
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,   # 追記により追加
    allow_methods=["*"],      # 追記により追加
    allow_headers=["*"]       # 追記により追加
)

url: str =  ${{secrets.SUPABSE_URL}}
key: str =  ${{secrets.SUPABSE_URL}}
print(url, key)
supabase = create_client(url, key)

class Item(BaseModel):
    name: str
    value: int

@app.get("/")
async def read_root():
    return {"message_System": "System is Active Now!!"}

@app.get("/Table/{table_name}")
async def get_apiinfo(table_name : str):
    response = supabase.table(table_name).select("*").match("Flag_Hidden", false).order('id', { ascending: false})
    return response.data

@app.get("/getTitle/")
async def get_titles():
    table_name = "Titles"
    reffered_table_column = "Articles(id, title)"
    response = supabase.table(table_name).select("*",reffered_table_column).eq("Flag_Hidden", "false").execute()
    return response.data

def print_spec() -> None:
    print(app.openapi())
