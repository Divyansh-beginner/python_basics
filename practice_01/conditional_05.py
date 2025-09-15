user_password: str = input("enter the password: ")
password_size: int = len(user_password)
if password_size<6 :
    strength: str = "Weak"
elif password_size<11:
    strength: str = "Medium"
else :
    strength: str = "Strong"
print(f"your password is of {password_size} length, which is {strength}!")

