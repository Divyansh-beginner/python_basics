import random
value:int = random.randint(0,2)
condition:list = [("green","Unripe"),("Yellow","Ripe"),("Brown","Overripe")]
print("picking a banana:")
print(f"this banana color is {condition[value][0]} and its in {condition[value][1]} state.")
exit()


