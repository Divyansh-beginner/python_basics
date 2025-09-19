import all_functions
input_n : int = int(input("enter the number :"))
input_pow : int = int(input("enter the power :"))
ans:int = all_functions.get_pow(input_n , input_pow)
print(f"{input_n} to power {input_pow} is {ans}")