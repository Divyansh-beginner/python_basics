import os
import all_functions

def main() :
    flag:bool = True

    while True :
        os.system("clear")
        print("yt videos manager app ! choose an option")
        print("1. To show the entire list of videos.")
        print("2. To add a video in the list.")
        print("3. To update a video details.")
        print("4. To delete a video.")
        print("5. To exit the app.")
        choice = input("Enter the choice number: ")

        try :
            all_functions.execute_choice(choice.strip())
        except all_functions.FileError :
            os.system("clear")
            print("There was a Fatal Error with the File, Exiting the App!")
            flag = False
        except all_functions.ExitLoop : 
            choice = input("Do you want to exit the App? \n press y for exit, press n or anything else to continue in the App.")
            if choice.strip() == "y" or choice.strip() == "Y": break
            else : continue

    if flag : os.system("clear")

if __name__ == "__main__" : main()

