# -------------------- ATM PIN CHECKER SYSTEM --------------------

balance = 5000
pin = 1234
attempts = 0
MAX_ATTEMPTS = 3

print("==== Welcome to the ATM System ====")

while attempts < MAX_ATTEMPTS:
    try:
        user_pin = int(input("Enter your 4-digit PIN: "))
    except ValueError:
        print("Invalid input! Please enter only numbers.\n")
        continue

    if user_pin == pin:
        print("\nPIN Verified Successfully.")
        print("Current Balance: ₹", balance)

        try:
            amount = int(input("Enter amount to withdraw: "))
        except ValueError:
            print("Invalid amount! Transaction cancelled.")
            break

        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > balance:
            print("Insufficient Balance.")
        else:
            balance -= amount
            print("Transaction Successful.")
            print("New Balance: ₹", balance)

        break

    else:
        attempts += 1
        print("Incorrect PIN! Attempts left:", MAX_ATTEMPTS - attempts, "\n")

if attempts == MAX_ATTEMPTS:
    print("Your account has been BLOCKED due to 3 incorrect PIN attempts.")
    print("Please contact the bank to reset your PIN.")
