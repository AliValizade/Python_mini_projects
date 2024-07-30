settings = {
    'upper': True,
    'lower': True,
    'symbol': True,
    'number': True,
    'space': False,
    'lenght': 8
}

def get_password_len_from_user(option, default, pw_min_len=8, pw_max_len=18):
    while True:
        user_input = input('Enter password lenght: '
                           f'(default value is {default}, (enter:default)) ')

        if user_input == '':
            return default
        
        if user_input.isdigit():
            if pw_min_len < int(user_input) <= pw_max_len:
                return int(user_input)
            else:
                print(f'Out of range, The lenght should be between ({pw_min_len}, {pw_max_len}): ')
        else:        
            print('Invalid input, enter a number: ')

        print('Try Again, Please! ')


def get_yes_or_no_from_user(option, default):
    while True:
        user_input = input(f'Include {option}, '
                           f'Default: {default}, (y:yes, n:no, enter:default)? ')

        if user_input == '':
            return default

        if user_input in ['y', 'n']:
            return user_input == 'y'
     
        print('Invalid input, Plz try again.(y/n/enter)')


def get_settings(settings):
    for option, default in settings.items():
        if option != 'lenght':
            user_choice = get_yes_or_no_from_user(option, default)
            settings[option] = user_choice
        else:
            password_len = get_password_len_from_user(option, default)
            settings[option] = password_len         


get_settings(settings)
print(settings)
