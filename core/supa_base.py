import flet as ft
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


def get_current_user(page: ft.Page):
    try:
        # Skontroluj, či máme uloženú session v page client storage
        access_token = page.client_storage.get("access_token")
        refresh_token = page.client_storage.get("refresh_token")

        # Skontroluj, či oba tokeny existujú
        if access_token and refresh_token:
            # Nastav session pre supabase klienta
            supabase = get_supabese_client()
            supabase.auth.set_session(access_token, refresh_token)
            return supabase.auth.get_session().user
        return None
    except Exception as ex:
        print(f"Error getting current user: {ex}")
        return None


def get_all_data(page: ft.Page):
    try:
        # Get current user id
        current_user_id = get_current_user(page).id
        
        # Get all data from current user
        supabase = get_supabese_client()
        response = supabase.table("users").select("*").eq("user_id", current_user_id).execute()

        return response.data
    except Exception as ex:
        print(f"Error getting all data: {ex}")
        return None
        
        
        
        
