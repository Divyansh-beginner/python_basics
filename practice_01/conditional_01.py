age: int = int(input("enter the age:"))
if age<0 or age>110 :
    print(f"{age} is not a valid age, please enter a valid age.")

elif(age<13):
    print(f"a child of {age} age.")

elif(age<20):
    print(f"a teen of {age} age.")

elif(age<60):
    print(f"a Adult of {age} age.")
else :
    print(f"a senior of {age} age.")

