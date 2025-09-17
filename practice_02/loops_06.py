n :int = int(input("enter the number: "))
if n<0 :
    print("enter a non-negative integer")

if n==0 or n==1 :
    print("ans : 1")

ans :int = 1
while n>0 :
    ans = ans*n
    n = n-1

print(f"ans: {ans}")
