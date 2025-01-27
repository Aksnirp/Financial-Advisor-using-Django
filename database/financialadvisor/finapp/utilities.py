import os
import sys
from sqlalchemy.exc import IntegrityError
from database.financialadvisor.financialadvisor.db_setup import Session_local
from django.apps import apps

# Adjust sys.path to ensure the correct module resolution
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))

def get_session():
    """
    Returns a new database session using SQLAlchemy.
    """
    return Session_local()

def get_users_model():
    -"""
    Lazily fetches the Users model using Django's apps.get_model.
    This avoids circular import issues.
    """
    return apps.get_model('finapp', 'Users')

# Function to sign up a user
def signup_u(username, email, password):
    """
    Adds a new user to the database. Handles potential IntegrityError if
    the email already exists in the database.

    Args:
        username (str): The username of the user.
        email (str): The email of the user.
        password (str): The user's password.

    Returns:
        dict: A dictionary indicating the status and message of the operation.
    """
    session = get_session()
    Users = get_users_model()  # Get the Users model lazily
    try:
        user = Users(
            username=username,
            email=email,
            password=password
        )
        session.add(user)
        session.commit()
        return {"status": "success", "message": f"User '{username}' added successfully!"}
    except IntegrityError:
        session.rollback()
        return {"status": "error", "message": f"A user with email '{email}' already exists."}
    except Exception as e:
        session.rollback()
        return {"status": "error", "message": f"Error adding user: {e}"}
    finally:
        session.close()
