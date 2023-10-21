from User import User
from datetime import date


class Account:
    __account = []
    __transection_history = []
    __loan_feature = True
    __loan_amount = 0

    def __init__(self, user_id) -> None:
        self.user_id = user_id
        if next((account for account in Account.__account if account['user']['id'] == self.user_id), None) is None:
            self.__account.append({
                'user': User.get_user(user_id),
                'balance': 0,
                'loan_times': 0,
                'loan_amount': 0
            })

    def get_account(self, account_number=None):
        if account_number is not None:
            account = None
            for index, user in enumerate(Account.__account):
                if user['user']['account_number'] == account_number:
                    account = user
                    break
            return account
        else:
            account = None
            for index, user in enumerate(Account.__account):
                if user['user']['id'] == self.user_id:
                    account = user
                    break
            return account

    def withdraw(self, amount):
        if amount > 0 and self.get_account(None)['balance'] > amount:
            self.get_account(None)['balance'] -= amount
            self.set_log(amount, 'Withdraw')
            return f"The amount {amount} has been withdrawn successfully.Now your balance is {self.get_account(None)['balance']}"
        else:
            return f"Withdrawal amount exceeded"

    def deposit(self, amount):
        if amount > 0:
            self.get_account(None)['balance'] += amount
            self.set_log(amount, 'Deposit')
            print(f'The amount {amount} is added to your account!')
        else:
            print('Please enter an amount greater than 0')

    def get_balance(self):
        return self.get_account(None)['balance']

    def get_log(self):
        for history in self.__transection_history:
            if (history['user']['id'] == self.user_id):
                print('User Name: ' + history['user']['name'])
                print('User Account: ' +
                      str(history['user']['account_number']))
                print('Transection Type: ' + history['transection_type'])
                print('Balance: ' + str(history['amount']))
            print('')

    def set_log(self, amount, type):
        self.__transection_history.append({
            'user': User.get_user(self.user_id),
            'date': date.today(),
            'amount': amount,
            'transection_type': type,
        })

    def get_loan(self, amount):
        if self.__loan_feature == False:
            print('The bank is bankrupt')
        elif self.get_account(None)['loan_times'] > 2:
            print('Sorry! You have already taken the loan 2 times!')
        else:
            self.get_account(None)['loan_amount'] += amount
            self.get_account(None)['loan_times'] += 1
            self.set_log(amount, 'Loan')
            self.__loan_amount += amount
            self.get_account(None)['balance'] += amount
            print('Loan Given.')

    @staticmethod
    def get_total_loan():
        return Account.__loan_amount

    @staticmethod
    def loan_feature_active_inactive(status):
        Account.__loan_feature = status
        if Account.__loan_feature == True:
            print('Loan Feature Activated Successfully!')
        else:
            print('Loan Feature Deactivated Successfully!')

    def transfer_balance(self, transfer_to, amount):
        if self.get_account(transfer_to) is not None:
            user = self.get_account(None)
            transfer_user = self.get_account(transfer_to)
            if transfer_user is None:
                print(f'{transfer_to} Account Number Not Found')

            elif amount == 0:
                print('Please enter an valid amount!')

            elif amount > user['balance']:
                print('Not Enough Balance in Your Account!')

            else:
                user['balance'] -= amount
                transfer_user['balance'] += amount
                self.set_log(amount, 'Send Money')
                print(f'{amount} Transfered successfully into account {transfer_to}')

    @staticmethod
    def all_user_account():
        return Account.__account

    @staticmethod
    def delete_account(account_number):
        user = None
        for index, user in enumerate(Account.__account):
            if user['user']['account_number'] == account_number:
                user = index
                break
        if user is not None:
            Account.__account.pop(user)
            return f'Account deleted'
