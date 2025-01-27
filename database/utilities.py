from setup import Session_local
from models import Users
from sqlalchemy import text

def get_session():
    return Session_local()

#adds the user after he sign up
def add_user(username,email):
    session = get_session()
    try:
        user = Users(username= username,email= email)
        session.add(user)
        session.commit()

    except Exception as e:
        session.rollback()
        print(f'error:{e}')
    finally:
        session.close()
        
def check():
    session = get_session()
    try:
        ...

    except Exception as e:
        print(f'error:{e}')
    finally:
        session.close()