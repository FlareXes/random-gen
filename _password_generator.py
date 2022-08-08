import sys
import random
import string
import secrets

PRINTABLE_CHARS = list(string.punctuation + string.digits + string.ascii_letters)

def secure_password(length=12):
    while True:
        password = ''.join(secrets.choice(PRINTABLE_CHARS) for i in range(length))

        if (sum(c.islower() for c in password) >= 2 and \
            sum(c.isupper() for c in password) >= 2 and \
            sum(c.isdigit() for c in password) >= 3):
            break
    return password

def random_text(length=10):
    return ''.join(random.choice(PRINTABLE_CHARS) for i in range(length))

if "__main__" == __name__:
    args = sys.argv
    invalid_args_msg = f"""
        USAGE: python _password_generator.py [text size]
        Example: python _password_generator.py 21\n
        [-] Invalid Input: '{args[1]}'
    """

    if len(args) > 1:
        try:
            length = int(args[1])
        except ValueError as e:
            print(invalid_args_msg)
            exit(1)
        if length > 11 and length < 1000001: 
            print(secure_password(length))
        else:
            print(random_text(length))
    else:
        print(secure_password())
