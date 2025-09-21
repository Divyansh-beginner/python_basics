from all_functions import variable_parameters_sum
import re

inputs:list[str] = re.findall("-[0-9]+|[0-9]+",input("enter the numbers: "))
inputs_in_int:list[int] = list(map(int,inputs))
sum_of_inputs:int = variable_parameters_sum(*inputs_in_int)
print(f"sum of {inputs_in_int} is: {sum_of_inputs}")
