class Console(object):
    def __init__(self):
        print('\nWelcome Database operation interface!')

    @staticmethod
    def displayOptions():
        print('\n[Please choose an option.]')
        print('{:12}'.format('1. Create'), end="")
        print('{:12}'.format('2. Search'), end="")
        print('{:12}'.format('3. Retrieve'))
        print('{:12}'.format('4. Update'), end="")
        print('{:12}'.format('5. Delete'), end="")
        print('{:12}'.format('6. Exit'))

    @staticmethod
    def getCommand():
        return input('choose : ')
