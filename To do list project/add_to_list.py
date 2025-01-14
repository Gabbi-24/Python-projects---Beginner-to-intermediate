import uuid       # Use to create a unique id
import os


# Get the script's exact path
script_dir = os.path.dirname(os.path.realpath(__file__))
# Set the exact script path as the new working directory
os.chdir(script_dir)


class AddToList:

    def __init__(self, list_name):
        self.list_name = list_name


    def create_list(self):
        try:
            stream = open(self.list_name, "w")
            stream.write("")

            stream.close()

        except Exception as e:
            print(f"There was an error: {e}")

    def add_item(self, task_item, deadline_item):
        id = str(uuid.uuid4())

        while True:
            try:
                stream = open(self.list_name, "a")
                stream.write(f"{id};{task_item};{deadline_item}\n")

                stream.close()
                break

            except Exception as e:
                print(f"There was an error: {e}")


# test_list = AddToList()
# test_list.create_list()

# test_list.add_item("Test task", "Test deadline")
# test_list.add_item("Test task 2", "Test deadline 2")
# test_list.add_item("Test task 3", "Test deadline 3")

