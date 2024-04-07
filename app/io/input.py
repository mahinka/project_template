import pandas as pd

def input_text_from_console():
    """Function to input text from the console.

    Returns:
        str: The text entered by the user.
    """
    return input("Write your text: ")

def read_text_from_file(file_path):
    """Function to read text from a file using built-in Python capabilities.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return "File not found"


def read_text_from_file_with_pandas(file_path):
    """Function to read text from a file using pandas library.

    Args:
        file_path (str): The path to the file to be read.

    Returns:
        str: The content of the file.
    """
    try:
        data = pd.read_csv(file_path)
        return data.to_string(index=False)
    except FileNotFoundError:
        return "File not found"