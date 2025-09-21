from all_functions import variable_keyword_args
from all_functions import variable_parameters_sum
dictonary:dict={"one":"first" , "two":22 , "three":{"innerdictkey":"innerdictvalue"}}
x = {10:"ten",20:"twenty",30:"thirty"}
variable_keyword_args(**dictonary)
print(variable_parameters_sum(*x))

