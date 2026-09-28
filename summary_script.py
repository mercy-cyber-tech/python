name = input("Name: ").strip().title()
program = input("program: ").strip().upper()
total_fees = float(input("total fees: "))
amount_paid = int(input("amount paid: "))
balance = total_fees - amount_paid
print(f"Balance: K{balance:,.2f}")