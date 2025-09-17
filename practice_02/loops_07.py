input_n:int = 11
flag : bool = True
while input_n<=1 or input_n>=10 :
    if flag :
        input_n : int = int(input("enter the number: "))
        flag = False
    else :
        input_n:int = int(input(f"input number {input_n} was not in range , enter number b/w 1 and 10: "))
else : 
    print(f"input number {input_n} was in range and accepted")
