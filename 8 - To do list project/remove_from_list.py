import os
from show_list import ShowList


# Get the script's exact path
script_dir = os.path.dirname(os.path.realpath(__file__))
# Set the exact script path as the new working directory
os.chdir(script_dir)


class CompletedTask:

    def __init__(self, list_name):     
        self.deleted_id = ""
        self.list_name = list_name


    def show_and_delete(self):
        try:
            stream = open(self.list_name)
            text = stream.read()
            while True:
                self.deleted_id = input("What is the ID of the completed item?: ")
                print("")
                if self.deleted_id in text:
                    break
                else:
                    print("The todo ID does not exist in your list. Please check that you have copied it correctly.")

        except Exception as e:
            print(f"Something went wrong with opening and reading the list: {e}")



    def update_list(self):
        try:
            # First we need to read the file and see what lines no not have the deleted id
            stream = open(self.list_name)
            new_lines = []
            for task in stream:
                if not self.deleted_id in task:
                    new_lines.append(task)

            stream.close()

            # Now we want to rewrite the todo list, excluding the completed task
            stream = open(self.list_name, "w")
            stream.writelines(new_lines)

            stream.close()


        except Exception as e:
            print(f"An error occurred: {e}")


# temp_show_current_list = ShowList()
# test_completed_task = CompletedTask(temp_show_current_list.show_list_items())
# test_completed_task.show_and_delete()
# test_completed_task.update_list()

