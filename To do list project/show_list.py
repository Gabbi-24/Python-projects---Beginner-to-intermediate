import os

# Get the script's exact path
script_dir = os.path.dirname(os.path.realpath(__file__))
# Set the exact script path as the new working directory
os.chdir(script_dir)


class ShowList:

    def __init__(self, list_name):
        self.task_as_list = []
        self.list_name = list_name


    def split_items(self):
        try:
            stream = open(self.list_name)
                
            for task in stream:
                task = list(task.split(";"))

                self.task_as_list.append(task)


            stream.close()


        except Exception as e:
            print(f"There was an error: {e}")


    def show_list_items(self):
        self.split_items()
        print(f"\n*** YOUR TASKS ***")
        if self.task_as_list != []:
            for task in self.task_as_list:
                print(f"{task[0]} | {task[1]} | {task[2]}", end = "")
            print("")
            return True

        else:
            print(f"You don't have any tasks right now.\n")
            return False




# test_show_list = ShowList()
# test_show_list.split_items()

# test_show_list.show_list_items()