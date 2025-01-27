import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from django.apps import AppConfig
from database.financialadvisor.financialadvisor.db_setup import init_db

class KickConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finapp'

    def ready(self):
        # Ensure the database is only initialized in specific cases
        
        try:
            print("Initializing the database...")
            init_db()
            print("Database initialized successfully.")
        except Exception as e:
            print(f"Error initializing database: {e}")