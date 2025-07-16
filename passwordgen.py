import string
import secrets
def genpass(length):
    lower=string.ascii_lowercase
    upper=string.ascii_uppercase
    dig=string.digits
    symb=string.punctuation

    char= lower + upper + dig + symb
    password = [
        secrets.choice(lower),
        secrets.choice(upper),
        secrets.choice(dig),
        secrets.choice(symb)
    ]

    for _ in range(length):
        password.append(secrets.choice(char))
    return ''.join(password)
inp=input("Enter the length of the password you want: ")
len=int(inp)
print(genpass(len))
