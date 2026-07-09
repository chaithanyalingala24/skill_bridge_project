from pydantic import BaseModel


# -----------------------------
# User Schemas
# -----------------------------
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    monthly_income: float
    monthly_expenses: float


class UserLogin(BaseModel):
    email: str
    password: str


# -----------------------------
# Loan Schemas
# -----------------------------
class LoanCreate(BaseModel):
    lender: str
    amount: float
    outstanding_amount: float
    emi: float
    interest: float
    overdue_days: int
    status: str