import sys
import os

# Add the parent directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..","..","..")))

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from database.financialadvisor.financialadvisor.db_setup import Base

class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer,primary_key=True)
    username = Column(String(80),nullable=False)
    email = Column(String(100),nullable=False,unique=True)
    password = Column(String(80),nullable=False)

class FinanceProfile(Base):
    __tablename__ = 'finance_profiles'

    profile_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)  # Foreign key linking to Users table
    financial_knowledge = Column(String(50), nullable=False)  # e.g., "Beginner," "Intermediate," "Expert"
    short_term_fluctuation_tolerance = Column(String(50), nullable=False)  # e.g., "Low," "Medium," "High"
    investment_horizon = Column(String(50), nullable=False)  # e.g., "Short Term," "Medium Term," "Long Term"
    age = Column(Integer, nullable=False)  # User's age
    risk_appetite = Column(String(50), nullable=False)  # e.g., "Low," "Medium," "High"
    financial_goal = Column(Text, nullable=False)  # Goal description