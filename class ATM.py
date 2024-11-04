class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.is_running = True

    def check_balance(self):
        print(f"Your current balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} deposited. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            self.balance -= amount
            print(f"${amount:.2f} withdrawn. New balance: ${self.balance:.2f}")

    def run(self):
        while self.is_running:
            print("\n--- ATM Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Select an option (1-4): ")
            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                self.is_running = False
            else:
                print("Invalid option. Please try again.")

if __name__ == "__main__":
    atm = ATM()
    atm.run()
