import os
from evaluate_choices import Choices
from add_to_list import AddToList


# Get the script's exact path
script_dir = os.path.dirname(os.path.realpath(__file__))
# Set the exact script path as the new working directory
os.chdir(script_dir)

# A function that allows you to create an empty todo list or overwrite an existing todo list with an empty list
def create_new_list(create_list_name):
    """
    Create an empty todo list or overwrite an existing todo list with an empty list.

    Parameters:
    create_list_name (str): The name of your list followed by '.txt'

    Returns:
    Creates a new text file in your current working directory
    """
    new_list = AddToList(create_list_name)
    new_list.create_list()


# A function that allows you to update any todo list that has already been created
def update_current_list(update_list_name):
    """
    Update any todo list that has already been created.

    Parameters:
    update_list_name (str): The full name of your list, including '.txt'

    Returns:
    Retrieves an existing text file from your current working directory.
    Initialises a console program to view and update a todo list by adding or completing items
    
    """
    choice_options = Choices(update_list_name)
    while not choice_options.exit:
        choice_options.choice_list()
        choice_options.evaluate_choice()




