settings = {
    'upper': True,
    'lower': True,
    'symbol': True,
    'number': True,
    'space': False,
    'lenght': 8
}


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


get_settings(settings)
print(settings)
