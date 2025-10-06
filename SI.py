try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time (in years): "))
    simple_interest = (principal * rate * time) / 100
    print(f"\nSimple Interest = {simple_interest:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
try:
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the annual interest rate (%): "))
    time = float(input("Enter the time (in years): "))
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    print(f"\nCompound Interest = {compound_interest:.2f}")
    print(f"Total Amount = {amount:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values only.")
