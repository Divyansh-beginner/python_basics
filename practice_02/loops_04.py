input_str : str = input("enter the string :")
size : int = len(input_str)
reverse_str: str = "".join([input_str[i] for i in range(size-1 , -1 , -1)])
print(reverse_str)
