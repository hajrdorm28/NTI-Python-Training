# احمد
def deposit(balance):
    amount = float(input("Enter Money: "))
    if amount <= 0:
        print("Failed")
        return balance
    balance += amount
    history.append("Deposited: " + str(amount) + " | New Balance: " + str(balance))
    print("Successfully")
    return balance

# جنى
def check_balance(balance):
    print("Current balance:", balance)


# هاجر
history = []
def transaction_history():
    if len(history) == 0:
        print("No transactions yet.")
    else:
        print("----- Transaction History -----")
        for record in history:
            print(record)
        print("--------------------------------")

def withdraw(balance):
    amount = float(input("Enter amount to withdraw: "))
    if amount <= 0:
        print("Amount must be positive.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance = balance - amount
        history.append("Withdrew: " + str(amount) + " | New Balance: " + str(balance))
        print("Withdrawal successful! New balance:", balance)
    return balance

# يوسف
def load_balance():
    file = open("atm.txt", "r")
    balance = float(file.readline())
    file.close()
    return balance

def main():
    balance = load_balance()
    while True:
        print("===== ATM SYSTEM =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")
        choice = input("Enter your choice: ")
        match choice:
            case "1":
                balance = deposit(balance)
            case "2":
                balance = withdraw(balance)
            case "3":
                check_balance(balance)
            case "4":
                transaction_history()
            case "5":
                print("Thank you")
                break
            case _:
                print("Invalid choice.")


                
main()