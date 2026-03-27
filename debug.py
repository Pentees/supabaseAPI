import os
import load_dotenv from dotenv

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
print(url, key)
