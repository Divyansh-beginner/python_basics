value is stored in __dict in key value format 
when want to make attributes private add __ infront of it , then only inside the function you can use it . 
actually when added __ in front of varible name , the variable name got mangeled and become self._Classname__varname , means now its stored in __dict as _Classname__varname key but inside the class or child class you can access this variable using only __varname ! its called automatic mangeling , where _Classname is added automatically , but setattr() doesn't do it , so have to do manual mangeling ! 
we can now only access these attributes from the object using obj._Classname__varname only ! and neither obj.varname nor obj.__varname will work ! 
automatic mangeling is only done for attributes which are actually define inside the class and not set by setattr()
to be noticed , inside any class self.__attribute always mangles with the class's names where it was written and not the objects class name ! it means if object was of child class whereas self.__attribute was used in parent class , then it would mangle the attribute name with parent class name rather than object's class(child) name ! 
if in a class its written like __class__ then it gives that class's name , but if written self.__class__ then it refers to the class whose object was made no matter where its written ! 
