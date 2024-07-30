import random
import string
import os

settings = {
    'upper': True,
    'lower': True,
    'symbol': True,
    'number': True,
    'space': False,
    'lenght': 8
}

PASSWORDW_MIN_LEN = 8
PASSWORDW_MAX_LEN = 20

def clear_screen():
    os.system('cls')


def get_password_len_from_user(option, default, pw_min_len=PASSWORDW_MIN_LEN, pw_max_len=PASSWORDW_MAX_LEN):
    while True:
        user_input = input('Enter password lenght: '
                           f'(default value is {default}, (enter:default)) ')

        if user_input == '':
            return default
        
        if user_input.isdigit():
            if pw_min_len <= int(user_input) <= pw_max_len:
                return int(user_input)
            else:
                print(f'Out of range ⛔, The lenght should be between ({pw_min_len}, {pw_max_len}): ')
        else:        
            print('Invalid input ❌, enter a number: ')

        print('Try Again, Please! ')


def get_yes_or_no_from_user(option, default):
    while True:
        user_input = input(f'📌 Include {option}❓ '
                           f'Default: {default}, (y:yes, n:no, enter:default) ')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
     
        print('Invalid input ❌, Plz try again.(y/n/enter)')


def get_settings(settings):
    for option, default in settings.items():
        if option != 'lenght':
            user_choice = get_yes_or_no_from_user(option, default)
            settings[option] = user_choice
        else:
            password_len = get_password_len_from_user(option, default)
            settings[option] = password_len


def ask_change_settings(settings):
    while True:
        user_answer = input('🚩 Do you want to change default settings❓ (y:yes, n:no, enter:yes) ')
        if user_answer in ['y', 'n', '']:
            if user_answer in ['y', '']:
                print('\n','-'*25, 'CHANGE SETTING', '-'*25, sep='')
                get_settings(settings)
            break
        else:
            print('Invalid input ❌, Please input (y/n) or press enter: ')


def generate_random_char(choices):
    choice = random.choice(choices)

    if choice == 'upper':
        return random.choice(string.ascii_uppercase)
    if choice == 'lower':
        return random.choice(string.ascii_lowercase)
    if choice == 'number':
        return random.choice(string.digits)
    if choice == 'symbol':
        return random.choice(string.punctuation)
    if choice == 'space':
        return ' '


def password_generator(settings):
    final_password = ''
    password_len = settings['lenght']

    choices = list(filter(lambda x: settings[x], ['upper', 'lower', 'symbol', 'number', 'space']))

    for i in range(password_len):
        final_password += generate_random_char(choices)

    return final_password


def ask_user_to_regenerate_password():
    while True:
        user_answer = input('📌 Do you want regenerate password❓ (y:yes, n:no, enter:yes) ')
        if user_answer in ['y', 'n', '']:
            if user_answer == 'n':
                return False
            return True
        else:
            print('Invalid input ❌, Please input (y/n) or press enter: ')


def password_generator_loop(settings):
    while True:
        print('=' * 62)
        print(f'📢 The generated password is: {password_generator(settings)}')

        if ask_user_to_regenerate_password() == False:
            break


def welcome():
    print('-'*15, 'WELCOME TO THE PASSWORD GENERATOR', '-'*15)
    print('-'*24, 'By: AliValizade', '-'*24, '\n')
    print('='*65)


def run():
    clear_screen()
    welcome()
    ask_change_settings(settings)
    password_generator_loop(settings)
    print('\nThanks for use our products.🙏❤')


run()
