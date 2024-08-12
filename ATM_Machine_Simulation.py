class ATM:
    def __init__(self):
        """Initialize the ATM system."""
        self.accounts = {}
        self.current_account = None

    def create_account(self, account_number, pin, initial_balance=0):
        """Create a new account with an initial balance."""
        if account_number in self.accounts:
            print("\nAccount already exists.")
            return False
        self.accounts[account_number] = {
            'pin': pin,
            'balance': initial_balance,
            'transaction_history': []
        }
        print("\nAccount created successfully.")
        return True

    def authenticate(self, account_number, pin):
        """Authenticate the user with account number and PIN."""
        if (account_number in self.accounts and
                self.accounts[account_number]['pin'] == pin):
            self.current_account = account_number
            print("\nAuthentication successful.")
            return True
        print("\nAuthentication failed.")
        return False

    def account_balance_inquiry(self):
        """Display the balance of the current account."""
        if not self.current_account:
            print("\nNo account authenticated.")
            return
        balance = self.accounts[self.current_account]['balance']
        print(f"\nCurrent balance: ₹{balance:.2f}")

    def cash_withdrawal(self, amount):
        """Withdraw cash from the current account."""
        if not self.current_account:
            print("\nNo account authenticated.")
            return
        if amount <= 0:
            print("\nInvalid withdrawal amount.")
            return
        account = self.accounts[self.current_account]
        if amount > account['balance']:
            print("\nInsufficient funds.")
            return
        account['balance'] -= amount
        account['transaction_history'].append(f"Withdrew ₹{amount:.2f}")
        print(f"\nWithdrawal of ₹{amount:.2f} successful.")

    def cash_deposit(self, amount):
        """Deposit cash into the current account."""
        if not self.current_account:
            print("\nNo account authenticated.")
            return
        if amount <= 0:
            print("\nInvalid deposit amount.")
            return
        account = self.accounts[self.current_account]
        account['balance'] += amount
        account['transaction_history'].append(f"Deposited ₹{amount:.2f}")
        print(f"\nDeposit of ₹{amount:.2f} successful.")

    def pin_change(self, new_pin):
        """Change the PIN for the current account."""
        if not self.current_account:
            print("\nNo account authenticated.")
            return
        if len(new_pin) != 4 or not new_pin.isdigit():
            print("\nInvalid PIN format. Must be 4 digits.")
            return
        self.accounts[self.current_account]['pin'] = new_pin
        print("\nPIN changed successfully.")

    def transaction_history(self):
        """Display the transaction history of the current account."""
        if not self.current_account:
            print("\nNo account authenticated.")
            return
        history = self.accounts[self.current_account]['transaction_history']
        if not history:
            print("\nNo transaction history.")
            return
        print("\nTransaction History:")
        for transaction in history:
            print(transaction)

def atm_simulation():
    """Simulate ATM operations."""
    atm = ATM()
    atm.create_account('12345', '0000', 69789)  # Sample account 1
    atm.create_account('67890', '1234', 987655)   # Sample account 2
    
    while True:
        print("\nATM Menu:")
        print("1. Authenticate")
        print("2. Account Balance Inquiry")
        print("3. Cash Withdrawal")
        print("4. Cash Deposit")
        print("5. PIN Change")
        print("6. Transaction History")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")
        
        if choice == '1':
            account_number = input("\nEnter account number: ")
            pin = input("\nEnter PIN: ")
            atm.authenticate(account_number, pin)
        elif choice == '2':
            atm.account_balance_inquiry()
        elif choice == '3':
            try:
                amount = float(input("\nEnter amount to withdraw: "))
                atm.cash_withdrawal(amount)
            except ValueError:
                print("\nInvalid amount. Enter a numeric value.")
        elif choice == '4':
            try:
                amount = float(input("\nEnter amount to deposit: "))
                atm.cash_deposit(amount)
            except ValueError:
                print("\nInvalid amount. Enter a numeric value.")
        elif choice == '5':
            new_pin = input("\nEnter new PIN (4 digits): ")
            atm.pin_change(new_pin)
        elif choice == '6':
            atm.transaction_history()
        elif choice == '7':
            print("\nExiting...")
            break
        else:
            print("\nInvalid choice. Try again.")

if __name__ == "__main__":
    atm_simulation()
