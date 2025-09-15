elements_in_str:str = input("enter the elements seperated by space:")
elements_list:list = elements_in_str.split()
neg_elements:list = [int(element) for element in elements_list if int(element)<0]
print(f"the negative elements are :{neg_elements} and count is {len(neg_elements)}")
