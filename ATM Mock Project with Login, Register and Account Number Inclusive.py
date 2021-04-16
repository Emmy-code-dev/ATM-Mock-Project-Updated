import random

data = {}


def man():
    is_valid = False
    print('Welcome to STANDARD CHATTERED BANK')

    while not is_valid:
        new_account = int(input(' Do you have any account with us\n'
                                'type (1) for Yes or (2) for No \n').lower())
        if new_account == 1:
            is_valid = True
            print('login to your account')
            login()
        elif new_account == 2:
            print('\n')
            ask = input('Do you wish to open an account with us ?:\n'
                        'Enter \'yes\' if you wish or Enter \'no\' if you do not wish to open an account with us \n ')

            if ask == 'yes'.lower():
                is_valid = True
                reg()
            else:

                print('\nThanks for banking with us.\n Have a nice Day')
                is_valid = True

        else:
            print("incorrect")
            man()


def bank_operation(user):
    check = True
    while check:
        print('\nWelcome %s %s'%(user[0],user[1]))
        currentBalance = 7000
        print('Welcome To Standard Chattered Atm %s' % user[0],user[1])
        print('Choose out of the available options: \n ')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')
        print('4. Logout')
        print('5. Exit')
        selected_option = int(input('Please select an option\n'))

        if selected_option == 1:

            print("How much would you like to withdraw")
            withdraw = int(input())
            print('Take your cash', withdraw, 'Naira\n Thank you for banking with us')
            check = False
        elif selected_option == 2:
            r_balance = int(input('How much would you like to deposit\n'))
            rem_balance = currentBalance + r_balance
            print('You deposited', r_balance,
                '\nYour Current balance is', rem_balance)
            check = False

        elif selected_option == 3:
            complaint = input('What issue will you like to report?\n')
            print('Your ',complaint,'is duely noted')
            print('Thanks for contacting us, Do have a nice day')
            check = False

        elif selected_option == 4:
            login()
            check = False

        elif selected_option == 5:
            print('Good Bye')
            exit()
        else:
            print('invalid option')
            check = False


def login():
    print('\n\n>>> Login <<<')
    isloginsuccessful = False

    while not isloginsuccessful:
        user_account = int(input('Enter your account number: \n'))
        password = input('Enter your password\n')

        for num, detail in data.items():
            if num == user_account:
                if detail[3] == password:
                    isloginsuccessful = True
                    bank_operation(detail)

            else:
                print('incorrect account')
                login()


def reg():
    print('\n>>> Register <<<\n')
    check = True
    print('fill in your information below')
    f_name = input('Enter your First name: ').capitalize()
    l_name = input('Enter your Last name: ').capitalize()
    password = input('Enter your Password: ')
    email = input('Enter your Email Address: ')
    while check:
        if '@' and '.com' not in email:
            print('\nincorrect email check your email and type again')
            reg()
        else:
            check = False
    act = account()
    data[act] = [f_name, l_name, email, password]
    print('Your account have been registered')
    print('\n Welcome to STANDARD CHATTERED BANK')
    print('\nYour account number is: ', act)
    login()

12
def account():
    return random.randrange(3031145278, 3126579211)


man()