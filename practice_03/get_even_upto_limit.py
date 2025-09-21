from all_functions import generate_even_nums_upto_limit
limit:int = int(input("enter the limit(limit is inclusive): "))
values_iterator:iter = generate_even_nums_upto_limit(limit)
for i in values_iterator:
    print(i)
