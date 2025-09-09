the python in shell(the one with >>>) is initialised by writing python in terminal, we don't need to write python3 because we installed a python-is-python3 alias .
its usually used for quick code or concept checks when whole new python file is not needed.
we have a inbuilt but not preimported module os , which could be imported in the python shell by direct import os.
it have some inbuilt functions like :
os.getcwd() to get current working directory.
import sys 
it have sys.platform inside it without () , which gives the platform its being running on , like linux for mine.
in python bash shell (one with >>>) it automatically searches for the imported thing in each file of current directory(i.e. python bash shell does mind where are you calling it , so call it in current directory to connect to the files) , so don't need to write from file_name import ..... , just write import method 
but if its outside of current directory (in parent folder ) then its better to just open the shell in that folder. otherwise the method is real messy
but if the file is in one of child's folder then you can import it by mentioning the child folder     name :  import child_folder.file 
also when importing the folder name can't be like 01_basics ! but basics_01 is allowed.
*** if something is changed inside a imorted folder after the import (talking about import in python shell here) , then that change is not going to show directly on the shell , even by importing again ! for it reopen the shell.

to counter the reopening of shell, a reload is available in importlib library(similar to sys)
>>>from importlib import reload
now write 
>>>reload(filename)//no filename.py because then it will try to search for something py named inside filename !
