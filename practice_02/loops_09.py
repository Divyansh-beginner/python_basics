items:list = ["apple", "banana", "orange", "apple", "mango"]
item_count:dict = {}
for item in items:
    if dict[item] != None:
        print(item)
        break 
    else :
        dict[item] = 1
