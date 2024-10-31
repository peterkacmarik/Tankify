
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from supabase import create_client, Client


# Načítaj .env súbor
load_dotenv()

# Ziskať hodnoty premennych
SUPABASE_USER = os.getenv("SUPABASE_USER")
SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")
SUPABASE_DB = os.getenv("SUPABASE_DB")
SUPABASE_PORT = os.getenv("SUPABASE_PORT")
SUPABASE_HOST = os.getenv("SUPABASE_HOST")
SUPABASE_PREFIX = os.getenv("SUPABASE_PREFIX")

# Vytvoriť engine
engine = create_engine(
    f"{SUPABASE_PREFIX}",
    connect_args={
        "host": f"{SUPABASE_HOST}",
        "port": f"{SUPABASE_PORT}",
        "database": f"{SUPABASE_DB}",
        "user": f"{SUPABASE_USER}",
        "password": f"{SUPABASE_PASSWORD}",
    }
)

def get_supabese_client() -> Client:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    supabase: Client = create_client(url, key)
    return supabase
