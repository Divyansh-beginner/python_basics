import datetime
today: str = datetime.date.today().strftime("%A")
age: int = int(input("enter the age:"))
price: int = 8 if age<18 else 12 
final_amount: int = price-2 if today == "Wednesday" else price
print(f"your final price is ${final_amount}")

