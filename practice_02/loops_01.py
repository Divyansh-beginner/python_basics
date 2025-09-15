import re
elements_string:str = input("enter the numbers of strings:")
negative_elements:list = list(map(int,re.findall("-[0-9]+",elements_string)))
print(f"all the negative numbers are:{negative_elements} and count is {len(negative_elements)}")
