ranges:int = int(input("enter the range:"))
even_numbers_sum:int = 0
even_numbers_sum:int =  sum([x for x in range(1,ranges+1) if x%2 == 0 ] , 0)
print(f"the sum of even numbers upto range {ranges} is {even_numbers_sum}")

