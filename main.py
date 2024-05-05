import secrets
import string

passlen = int(input("Enter password length:"))
alpha = string.ascii_letters+string.digits
password = ''.join(secrets.choice(alpha) for i in range(passlen))

def password_Strength(password):
    length = len(password)
    if length<8:
        return "Weak"
    elif length <12:
        return "Moderate"
    else:
        return "Strong"
print("Your password is:",password)
print("Your password strength:",password_Strength(password))

