import re
it can give many useful tools for a string(only strings) and could give lists based on the seperations.
like re.findall("regex",the_string) will give a list of only those strings selected from the the_string that passes the regex criteria : ex for negative numbers enter "-[0-9]+" , for both postive or negative numbers : "[0-9]+|-[0-9]+" etc.
re.split("regex",the_string) will give the list of strings after splitting them based on the regex criteria.
the map(function , iterable) will return a map object , it runs the function on all elements of the iterable and then store them. 
we can convert the map obj into list if want using the list(map(func , iterable)) or into string or tuple or similar too.

the sum(iterable , inital_value_0_at_default) gives sum of all numbers inside iterable , works when iterable has numbers , reject if other.
