import datetime
year:int = datetime.date.today().year
if year%400 ==0 :
    leap: str = "leap year"
elif year%4 ==0 and year%100 != 0:
    leap: str = "leap year" 
else :
    leap: str = "not a leap year"
print(f"this year is {leap}")
