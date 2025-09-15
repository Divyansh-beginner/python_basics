import datetime module gives access to today's date and weekday
datetime.date.today() gives today's date
datetime.date.today().weekday() gives today's weekday in numbers: 0->monday , 1->tuesday, ....
datetime.date.today().strftime(%A) gives weekday full english name in camelcase like : Monday, ...
can get month or year using datetime.date.today().month or .year , no () because month and year are just names inside output obj of .today() (ie today() gives an obj output that has .weekday() , .strftime() , .year , .month, day )

import bisect 
the bisect.bisect(sorted_list_ascending_of_ints, value) gives the index at which the value should be placed ! if the value is equal to an element then it will pass/jump it will place the value after that element 


