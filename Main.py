from User import User
from Account import Account
from Admin import Admin

logged_in_user = None
logged_in_admin = None


def user_login(email, password):
    user = next((user for user in User.get_user()
                if user['email'] == email), None)
    if user is not None and user['password'] == password:
        global logged_in_user
        logged_in_user = user['id']
        print("Logged in successfully")
    else:
        print("Your email or password not valid!")


def admin_login(email, password):
    admin = next((admin for admin in Admin.get_admin()
                 if admin['email'] == email), None)
    if admin is not None and admin['password'] == password:
        global logged_in_admin
        logged_in_admin = admin['id']
        print("Logged in successfully")
    else:
        print("Your email or password not valid!")


def main():
    print("============= User Section ===============")
    print('User Login: 1')
    print('User Sign up: 2')
    print('Withdraw: 3')
    print('Deposit: 4')
    print('Check available balance: 5')
    print('Check transection history: 6')
    print('Take Loan: 7')
    print('Transfer Balance: 8')
    print('See Others Account Numbers: 9')
    print("============= User Section ===============")
    print('')
    print("============= Admin Section ===============")
    print('Admin Login: 10')
    print('Admin Sign up: 11')
    print('Delete User Account: 12')
    print('User Account List: 13')
    print('Total Available Balance: 14')
    print('Total Loan Amount : 15')
    print('ON/OFF Loan Feature : 16')
    print("============= Admin Section ===============")
    print('')

    while True:

        command = int(input('Press a key: '))
        # if logged_in_user is not None:
        # account = Account(logged_in_user)

        if command == 1:
            print('User Login:')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            user_login(email, password)
            print('')

        if command == 2:
            print('User sign up and account create: ')
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            address = input('Enter your address: ')
            account_type = input('Enter account type: (Savings, Current)')
            password = input('Enter your password: ')
            user = User(name, email, address, account_type, password)
            account = Account(user.current_user())
            print('')

        if command == 3:
            if logged_in_user is not None:
                amount = float(input('Enter an amount: '))
                print(account.withdraw(amount))
            else:
                print('Please Login First')
            print('')

        if command == 4:
            if logged_in_user is not None:
                amount = float(input('Enter an amount: '))
                account.deposit(amount)
            else:
                print('Please Login First')
            print('')

        if command == 5:
            if logged_in_user is not None:
                print(f'Available balance is: {account.get_balance()}')
            else:
                print('Please Login First')
            print('')

        if command == 6:
            if logged_in_user is not None:
                print("=============Transection History===================")
                account.get_log()
                print("=============Transection History===================")
            else:
                print('Please Login First')
            print('')

        if command == 7:
            if logged_in_user is not None:
                amount = float(input('Enter an amount: '))
                if amount > 0:
                    account.get_loan(amount)
                else:
                    print('Please enter an amount greater than 0.')
            else:
                print('Please Login First')

        if command == 8:
            if logged_in_user is not None:
                acc_number = input('Enter an account number: ')
                amount = float(input('Enter an amount: '))
                account.transfer_balance(acc_number, amount)
            else:
                print('Please Login First')

        if command == 9:
            if logged_in_user is not None:
                for val in User.get_user():
                    if val['id'] != logged_in_user:
                        print(val['account_number'], end=' ')
                print('')
            else:
                print('Please Login First')

        if command == 10:
            print('Admin Login:')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            admin_login(email, password)
            print('')

        if command == 11:
            print('Admin sign up: ')
            name = input('Enter your name: ')
            email = input('Enter your email: ')
            password = input('Enter your password: ')
            admin = Admin(name, email, password)
            print('')

        if command == 12:
            if logged_in_admin is not None:
                account_number = input('Enter an account_number to delete: ')
                User.delete_user(account_number)
                Account.delete_account(account_number)
            else:
                print('Please Login First')

        if command == 13:
            print("============== All user accounts ============= : ")
            if logged_in_admin is not None:
                print(Account.all_user_account())
            else:
                print('Please Login First')
            print("============== All user accounts ============= : ")
            print('')

        if command == 14:
            if logged_in_admin is not None:
                t_amount = 0
                for acc in Account.all_user_account():
                    t_amount += acc['balance']
                print(f"Total balance of the bank : {t_amount}")
            else:
                print('Please Login First')

        if command == 15:
            if logged_in_admin is not None:
                print(f"Total Loan : {Account.get_total_loan()}")
            else:
                print('Please Login First')

        if command == 16:
            if logged_in_admin is not None:
                user_input = input("Type True /False : ")
                if user_input == 'True':
                    Account.loan_feature_active_inactive(True)
                elif user_input == 'False':
                    Account.loan_feature_active_inactive(False)
            else:
                print('Please Login First')


if __name__ == "__main__":
    main()
