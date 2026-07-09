from sqlalchemy import Column, Integer, String, Float
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    email = Column(String, unique=True, nullable=False)

    password = Column(String, nullable=False)

    monthly_income = Column(Float, default=0)

    monthly_expenses = Column(Float, default=0)


class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)

    lender = Column(String, nullable=False)

    amount = Column(Float, nullable=False)

    outstanding_amount = Column(Float, nullable=False)

    emi = Column(Float, nullable=False)

    interest = Column(Float, nullable=False)

    overdue_days = Column(Integer, default=0)

    status = Column(String, default="Active")