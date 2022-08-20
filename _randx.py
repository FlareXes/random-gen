import sys
import random
import string
import secrets

AMBIGUOUS_CHARS = {",", ".", ";", ":", "\\", "/", "'", '"', "~", "(", ")", "{", "}", "[", "]", "`", "^", "<", ">", "1", "l", "L", "I", "0", "o", "O"}
PRINTABLE_CHARS = list(string.punctuation + string.digits + string.ascii_letters)
PRINTABLE_SAFE_CHARS = list(set(PRINTABLE_CHARS).difference(AMBIGUOUS_CHARS))

def secure_password(char_list, length=16):
    while True:
        password = ''.join(secrets.choice(char_list) for i in range(length))

        if (sum(c.islower() for c in password) >= 2 and \
            sum(c.isupper() for c in password) >= 2 and \
            sum(c.isdigit() for c in password) >= 3):
            break
    return password

def random_text(length, char_list):
    return ''.join(random.choice(char_list) for i in range(length))

if "__main__" == __name__:
    args = sys.argv
    args_len = len(args)
    
    if  args_len > 1 and  args_len < 5:
        for i in args:
            try:
                length = int(i)
                break
            except ValueError:
                length = 16

        if length > 11 and length < 1000001:
            if "--safe" not in args:
                print(secure_password(PRINTABLE_CHARS, length))
            else:
                print(secure_password(PRINTABLE_SAFE_CHARS, length))
        else:
            if "--safe" not in args:
                print(random_text(length, PRINTABLE_CHARS))
            else:
                print(random_text(length, PRINTABLE_SAFE_CHARS))
    else:
        print(secure_password(PRINTABLE_CHARS))
