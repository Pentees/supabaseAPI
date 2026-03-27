import os
from dotenv import load_dotenv

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
print(url, key)
