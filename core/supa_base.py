import flet as ft
import os
from dotenv import load_dotenv
# from sqlalchemy import create_engine
from supabase import create_client, Client
# from config import Config
from locales.localization import LocalizedText

# config = Config()

# Načítaj .env súbor
load_dotenv()

# Ziskať hodnoty premennych
# SUPABASE_USER = os.getenv("SUPABASE_USER")
# SUPABASE_PASSWORD = os.getenv("SUPABASE_PASSWORD")
# SUPABASE_DB = os.getenv("SUPABASE_DB")
# SUPABASE_PORT = os.getenv("SUPABASE_PORT")
# SUPABASE_HOST = os.getenv("SUPABASE_HOST")
# SUPABASE_PREFIX = os.getenv("SUPABASE_PREFIX")

# Vytvoriť engine
# engine = create_engine(
#     f"{SUPABASE_PREFIX}",
#     connect_args={
#         "host": f"{SUPABASE_HOST}",
#         "port": f"{SUPABASE_PORT}",
#         "database": f"{SUPABASE_DB}",
#         "user": f"{SUPABASE_USER}",
#         "password": f"{SUPABASE_PASSWORD}",
#     }
# )

def get_supabese_client() -> Client:
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_KEY")
    # url = config.SUPABASE_URL
    # key = config.SUPABASE_KEY
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


class SupabaseUser:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.supabase = get_supabese_client()
        # self.lang_manager = LanguageManager(self.page)

    def create_user_in_table_users(self, page: ft.Page, user_data: dict):
        try:
            # Get current user id
            current_user_id = get_current_user(page).id
            if not current_user_id:
                raise Exception("No user is currently logged in")

            # Pridanie user_id do údajov
            user_data["user_id"] = current_user_id

            # Vloženie údajov do tabuľky users
            response = self.supabase.table("users").insert(user_data).execute()

            # return response.data
        except Exception as ex:
            print(f"Error creating user: {ex}")
            return None


    def get_all_data_from_table_users(self, page: ft.Page):
        try:
            # Get current user id
            current_user_id = get_current_user(page).id
            response = self.supabase.table("users").select("*").eq("user_id", current_user_id).execute()

            return response.data
        except Exception as ex:
            print(f"Error getting all user data: {ex}")
            return None


    def delete_user_from_table_users(self, page: ft.Page, user_id):
        try:
            response = self.supabase.table("users").delete().eq("id", user_id).execute()
            page.open(ft.SnackBar(content=ft.Text(self.lang_manager.get_translation("msg_excluir_sucesso"))))
            page.go("/users")
            page.update()

            # return response
        except Exception as ex:
            print(f"Error getting all data: {ex}")
            return None


    def update_user_in_table_users(self, user_id, user_data: dict):
        try:
            update_data = {
                "name": user_data["name"].content.value,
                "email": user_data["email"].content.value,
                "user_type": user_data["user_type"].content.value,
                "driver_license_category": user_data["driver_license_category"].content.value,
                "driver_license_expiry": user_data["driver_license_expiry"].content.controls[1].value,
                "is_active": user_data["is_active"].content.value,
                "vehicle_user": user_data["vehicle_user"].content.value,
            }

            # Vloženie údajov do tabuľky users
            response = (
                self.supabase.table("users")
                .update(update_data)
                .eq("id", user_id)
                .execute()
            )
            # return response.data
        except Exception as ex:
            print(f"Error updating user: {ex}")
            return None


    def get_vehicle_names(self, page):
        try:
            # Get current user id
            current_user_id = get_current_user(page).id
            # Get vehicle name from supabase
            response: dict = self.supabase.table("vehicles").select("name").eq("vehicle_id", current_user_id).execute()
            names: list = [name["name"] for name in response.data]
            # Return vehicle name
            return names
        except Exception as ex:
            print(f"Error getting all data: {ex}")
            return []


class SupabaseVehicle:
    def __init__(self, page: ft.Page) -> None:
        self.page = page
        self.supabase = get_supabese_client()

    def get_all_data_from_table_vehicles(self):
        try:
            # Get current user id
            current_user_id = get_current_user(self.page).id
            response = self.supabase.table("vehicles").select("*").eq("vehicle_id", current_user_id).execute()

            return response.data
        except Exception as ex:
            print(f"Error getting all vehicle data: {ex}")
            return None


    def create_vehicle_in_table_vehicles(self, page: ft.Page, vehicle_data: dict):
        try:
            # Get current user id
            current_user_id = get_current_user(page).id
            if not current_user_id:
                raise Exception("No user is currently logged in")

            # Pridanie user_id do údajov
            vehicle_data["vehicle_id"] = current_user_id

            # Vloženie údajov do tabuľky users
            response = self.supabase.table("vehicles").insert(vehicle_data).execute()

            # return response.data
        except Exception as ex:
            print(f"Error creating vehicle: {ex}")
            return None


    def delete_vehicle_from_table_vehicles(self, page: ft.Page, vehicle_id, loc, dialog):
        try:
            response = self.supabase.table("vehicles").delete().eq("id", vehicle_id).execute()
            page.open(ft.SnackBar(content=LocalizedText(loc, "msg_excluir_sucesso")))
            # page.go("/vehicles")
            page.close(dialog)
            page.update()

            # return response
        except Exception as ex:
            print(f"Error getting all data: {ex}")
            return None


    def update_vehicle_in_table_vehicles(self, vehicle_id, vehicle_data: dict):
        try:
            # Vloženie údajov do tabuľky users
            response = (
                self.supabase.table("vehicles")
                .update(vehicle_data)
                .eq("id", vehicle_id)
                .execute()
            )
            if response.data:
                return response.data
            else:
                print("No data returned from update operation")
                return None
        except Exception as ex:
            print(f"Error updating vehicle: {ex}")
            return None


