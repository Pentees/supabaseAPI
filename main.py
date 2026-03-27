
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

url: str =  os.environ.get("URL")
key: str =  os.environ.get("KEY")

supabase = create_client(url, key)

@app.get("/supabaseAPI/getTitle/")
async def get_titles():
    table_name = "Titles"
    reffered_table_column = "Articles(id, title)"
    response = supabase.table(table_name).select("*",reffered_table_column).eq("Flag_Hidden", "false").execute()
    return response.data
    
@app.get("/supabaseAPI/getData/{id}")
async def get_Data(id: str):
    print(id)
    response = supabase.table("Articles").select("*", "Titles(created_at, language)").eq("id", id).execute()
    return response.data

def print_spec() -> None:
    print(app.openapi())
