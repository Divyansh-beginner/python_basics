from all_functions import print_choices, execute_choice, ExitLoop, get_final_choice_to_exit_app

def main():
    while True:
        print_choices()
        choice = input("Enter the choice number: ").strip()
        try:
            execute_choice(choice)
        except ExitLoop : 
            final_choice = get_final_choice_to_exit_app()
            if final_choice : break
            
if __name__=="__main__":main()

        