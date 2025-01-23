import os
from add_to_list import AddToList
from show_list import ShowList
from remove_from_list import CompletedTask


# Get the script's exact path
script_dir = os.path.dirname(os.path.realpath(__file__))
# Set the exact script path as the new working directory
os.chdir(script_dir)


class Choices:

    def __init__(self, list_to_update):      # Input an object from add_to_list
        self.choice = ""
        self.exit = False
        self.list_to_update = list_to_update
        self.list_object = AddToList(self.list_to_update)


    def choice_list(self):
        print("""
*** TODO LIST OPTIONS ***
[1] Show tasks
[2] Add tasks
[3] Complete task
[4] Exit
""")
        
        while True:
            try:
                self.choice = int(input("What do you want to do? (Choose option number): "))
                if self.choice in [1, 2, 3, 4]:
                    break
                else:
                    print(f"\nPlease choose from only numbers 1 to 4.\n")
            
            except ValueError:
                print(f"\nInvalid input: Please type a numeric input from 1 to 4.\n")
        

    def evaluate_choice(self):
        if self.choice == 1:
            show_list = ShowList(self.list_object.list_name)
            show_list.show_list_items()

        elif self.choice == 2:
            while True:
                specify_task = input("What is the task?: ")
                if ";" in specify_task:
                    print(f"\nPlease don't use ';' in your input.\n")
                else:
                    break
            while True:
                specify_deadline = input("What is the deadline?: ")
                if ";" in specify_deadline:
                    print(f"\nPlease don't use ';' in your input.\n")
                else:
                    break
            self.list_object.add_item(specify_task, specify_deadline)

        elif self.choice == 3:
            completed_task = CompletedTask(self.list_object.list_name)
            current_list = ShowList(self.list_object.list_name)
            if current_list.show_list_items():
                completed_task.show_and_delete()
                completed_task.update_list()
            else:
                print(f"All your tasks are complete!\n")

        elif self.choice == 4:
            print(f"Good bye...\n")
            self.exit = True




