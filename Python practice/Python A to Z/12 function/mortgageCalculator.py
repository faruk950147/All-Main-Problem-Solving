# def mortgageCalculator(principal, rate, years):
#     monthly_rate = rate / 12
#     months = years * 12
#     monthly_payment = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
#     return monthly_payment

# print(mortgageCalculator(100000, 5, 30))

def calculate_mortgage(principal, annual_interest_rate, years):
    # monthly interest rate = annual interest rate that means case yearly interest rate ÷ 12 ÷ 100
    monthly_interest_rate = annual_interest_rate / 12 / 100
    months = years * 12

    # monthly payment = principal × monthly interest rate × (1 + monthly interest rate)months / ((1 + monthly interest rate)months - 1)
    if monthly_interest_rate == 0:
        emi = principal / months
    else:
        emi = principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / \
              ((1 + monthly_interest_rate) ** months - 1)

    total_payment = emi * months
    total_interest = total_payment - principal

    return emi, total_interest, total_payment


# input
principal = float(input("Loan amount: "))
annual_interest_rate = float(input("Interest rate (Annual %): "))
years = int(input("Loan term (Years): "))

# calculate
emi, total_interest, total_payment = calculate_mortgage(principal, annual_interest_rate, years)

# output
print(f"\nMonthly Payment (EMI): {emi:.2f}")
print(f"Total Interest: {total_interest:.2f}")
print(f"Total Payment: {total_payment:.2f}")
