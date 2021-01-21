# Bank account
# Step 1: Create bank account class
class Account():

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f'Account owner: {self.owner}\nAccount balance: ${self.balance}'

    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        print(f'${deposit_amount} Deposit Accepted!\nNew balance: {self.balance}')

    def withdraw(self, withdraw_amount):
        if self.balance >= withdraw_amount:
            self.balance -= withdraw_amount
            print(f'${withdraw_amount} Withdrawal accepted!\nNew balance: {self.balance}')
        else:
            print('Funds Unavailable!')


# Step 2: Create Login class
def login(Account):
    user_name = ''
    pass_word = ''

    while user_name != 'a1' and pass_word != 1234:
        user_name = input('Please enter username:\n')
        pass_word = input('Please enter password:\n')

        if user_name == 'a1' and pass_word == '1234':
            # Step 3: Instantiate the class
            accnt1 = Account('Ali', 0)
            print(f'Welcome {accnt1.owner}!\nYour account balance is ${accnt1.balance}')
        else:
            print('Username or password is wrong! Please try again.\n')

# Step 3: Call login class
login(Account)


# Step 4: Create start transaction class
def start_transaction():
    # Instantiate Account class
    accnt1 = Account('Ali', 0)
    continue_trans = True
    while continue_trans == True:
        transaction_type = input('To deposit press 1, To withdraw press 2, To end press 3\n')

        if transaction_type not in ['1', '2', '3']:
            print("Sorry, wrong input! please choose 1 or 2 \n")

        if transaction_type == '1':
            deposit_amount = int(input('Please enter the deposit amount\n'))
            accnt1.deposit(deposit_amount)
        elif transaction_type == '2':
            withdraw_amount = int(input('Please enter the withdraw amount\n'))
            accnt1.withdraw(withdraw_amount)

        else:
            print('Thank you and goodbye!')
            return continue_trans == False

# Step 5: Call start transaction class
start_transaction()
