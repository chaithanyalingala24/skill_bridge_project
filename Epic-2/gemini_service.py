import os
from dotenv import load_dotenv

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY", "")
print("API KEY =", GOOGLE_API_KEY)


def _call_gemini(prompt: str):

    if not GOOGLE_API_KEY:
        print("Gemini API key not found.")
        return None

    try:
        genai = importlib.import_module("google.generativeai")

        genai.configure(api_key=GOOGLE_API_KEY)

        model = genai.GenerativeModel("gemini-2.5-flash")

        response = model.generate_content(prompt)

        return response.text

    except ImportError:
        print("Gemini package not installed.")
        return None

    except Exception as e:
        print(f"Gemini Error: {e}")
        return None


def generate_strategy(user, loans):

    prompt = f"""
    User Monthly Income: {user.monthly_income}
    User Monthly Expenses: {user.monthly_expenses}

    Loans:
    {loans}

    Generate a professional loan settlement strategy.
    """

    result = _call_gemini(prompt)

    if result:
        return result

    return """
    1. Contact lenders with highest interest rate first.
    2. Request settlement discounts.
    3. Prioritize overdue loans.
    4. Negotiate lower EMI plans.
    5. Maintain regular communication.
    """


def generate_email(user, loan):

    prompt = f"""
    Write a professional loan settlement request email.

    User Name: {user.name}

    Lender: {loan.lender}

    Outstanding Amount: {loan.outstanding_amount}
    """

    result = _call_gemini(prompt)

    if result:
        return result

    return f"""
Subject: Loan Settlement Request

Dear {loan.lender},

I hope you are doing well.

I am facing temporary financial difficulties and request consideration for a settlement or revised repayment plan.

Outstanding Amount: ₹{loan.outstanding_amount}

Thank you for your support.

Regards,
{user.name}
"""