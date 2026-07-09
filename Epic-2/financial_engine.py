from typing import List

def calculate_financial_health(user, loans):
    """
    Calculate financial health metrics
    """

    total_emi = sum(loan.emi for loan in loans)

    total_outstanding = sum(loan.outstanding_amount for loan in loans)

    surplus = user.monthly_income - user.monthly_expenses - total_emi

    if user.monthly_income > 0:
        emi_ratio = (total_emi / user.monthly_income) * 100
    else:
        emi_ratio = 0

    if user.monthly_income > 0:
        debt_to_income = (total_outstanding / user.monthly_income) * 100
    else:
        debt_to_income = 0

    if emi_ratio > 50:
        stress_level = "High"
    elif emi_ratio >= 30:
        stress_level = "Medium"
    else:
        stress_level = "Low"
    return {
        "total_emi": total_emi,
        "total_outstanding": total_outstanding,
        "surplus": surplus,
        "emi_ratio_percent": round(emi_ratio, 2),
        "debt_to_income_percent": round(debt_to_income, 2),
        "stress_level": stress_level,
        "total_loans": len(loans)
    }

def calculate_loan_priority(loans):
    """
    Assign priority to each loan based on
    interest rate, overdue days and EMI.
    """

    prioritized_loans = []

    for loan in loans:

        if loan.interest > 15 or loan.overdue_days > 30:
            priority = "High"

        elif loan.interest > 10 or loan.overdue_days > 15:
            priority = "Medium"

        else:
            priority = "Low"

        prioritized_loans.append({
            "lender": loan.lender,
            "amount": loan.outstanding_amount,
            "interest": loan.interest,
            "overdue_days": loan.overdue_days,
            "priority": priority
        })

    return prioritized_loans

def simulate_debt_timeline(loans):
    """
    Simulate monthly debt repayment timeline.
    """

    timeline = []

    for loan in loans:

        balance = loan.outstanding_amount

        month = 1

        while balance > 0:

            timeline.append({
                "lender": loan.lender,
                "month": month,
                "remaining_balance": max(balance, 0)
            })

            balance -= loan.emi
            month += 1

    return timeline

def predict_settlement(user, loans):
    """
    Predict settlement percentage and risk score.
    """

    total_emi = sum(loan.emi for loan in loans)
    total_outstanding = sum(loan.outstanding_amount for loan in loans)

    if user.monthly_income > 0:
        emi_ratio = (total_emi / user.monthly_income) * 100
    else:
        emi_ratio = 0

    if user.monthly_income > 0:
        debt_to_income = (total_outstanding / user.monthly_income) * 100
    else:
        debt_to_income = 0

    settlement_results = []

    for loan in loans:

        settlement = 50.0
        risk_score = 0

        if loan.overdue_days > 0:
            settlement += 5
            risk_score += 20

        if emi_ratio > 50:
            settlement += 5
            risk_score += 15

        if loan.interest > 12:
            settlement += 5
            risk_score += 10

        if debt_to_income > 80:
            settlement += 5
            risk_score += 15

        settlement = max(40, min(75, settlement))

        if risk_score >= 40:
            risk_category = "High"
        elif risk_score >= 20:
            risk_category = "Medium"
        else:
            risk_category = "Low"

        settlement_results.append({
            "loan_id": loan.id,
            "lender": loan.lender,
            "outstanding_amount": loan.outstanding_amount,
            "interest": loan.interest,
            "emi": loan.emi,
            "suggested_settlement_percentage": settlement,
            "risk_score": risk_score,
            "risk_category": risk_category
        })

    return settlement_results