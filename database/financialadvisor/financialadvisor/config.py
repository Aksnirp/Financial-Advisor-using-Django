from dotenv import load_dotenv
from urllib.parse import quote
import os

# Load environment variables from .env
#dotenv_path = os.path.join(os.path.dirname(__file__), '../../.env')
dotenv_path='./.env'
print(f"Loading .env from: {dotenv_path}")  # Debugging line
load_dotenv(dotenv_path=dotenv_path)

# Read variables
DB_HOST = os.getenv('db_host')
DB_USER = os.getenv('db_user')
DB_PASSWORD = os.getenv('db_password')
DB_NAME = os.getenv('db_name')
DB_PORT = os.getenv('db_port')

# Debugging: Print values (hide passwords for security)
print(f"DB_HOST: {DB_HOST}, DB_USER: {DB_USER}, DB_PORT: {DB_PORT}, DB_NAME: {DB_NAME}")

if None in [DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT]:
    raise ValueError("One or more database environment variables are not set! Check .env file.")

