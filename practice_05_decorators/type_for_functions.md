the functions give "function" when want to see their types with type(func) , but its not what you enter when want to show their type ! like : in decorators , or when you do x = y , where y is actually a function , here you can't do :
x:function = y , neither x:func = y nor x:def = y ! 
its actually a Callable , with Capital C , where Callable[inputarg1type , inputarg2type , ........ , returntype] , or can do Callable[Any , Any] where first Any means takes anything as argument and second Any means could give/return any type. also its Any with capital A .
or you could do : Callable[[...] , Any] exactly three ... means any number of args with Any in return . 

callable with small c is actually a inbuilt method used to check if something is a function/Callable or not ! ie callable(y) gives true if y is a method/function/Callable .

any with small a is also a inbuilt method thats used to check is something is a iterable or not , i.e.  any(x) gives True if x is a list , tuple , generator , dict , even strings 
