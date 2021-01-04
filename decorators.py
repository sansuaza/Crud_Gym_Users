PASSWORD_KEY = 'surekey'

def need_key_authorization(func):
    def wrapper():
        password_from_client = input('Enter the password to complete de requirement: ')
        if PASSWORD_KEY == password_from_client:
            return func()

        else:
            print('error, the password key does not match')

    return wrapper

@need_key_authorization
def process_with_key_requited():
    print('process succesfully')

if __name__ == '__main__':
    process_with_key_requited()