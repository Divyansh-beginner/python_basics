# prime number checker:
n : input = int(input("enter the number :"))
max_l:int = int(n/2 )+1
flag : bool = True
if n !=2:
    for i in range(2 , max_l+1 , 1):
        if n%i == 0 : 
            print(f"entered number {n} is divisible by {i} ")
            flag = False
            break
if flag : 
    print(f"number {n} was prime!")
