input_str:str = input("enter the string: ")
flag: bool = True
flag2: bool = True
for i in range(0 , len(input_str)-1):
    if input_str[i] != input_str[i+1] :
        if flag :
            print(input_str[i])
            flag2 = False
            break
        else :
            flag = True
    else :
        flag = False
if flag2 and flag : 
    print(input_str[len(input_str)-1])
    flag2 = False
if flag2 :
    print("all characters are repeating") 
    