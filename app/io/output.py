import pandas as pd


def output_text_to_console(text):
    """Function to output text to the console.

    Args:
        text (str): The text to be printed.
    """
    print(text)


def write_text_to_file(text, file_path):
    """Function to write text to a file using built-in Python capabilities.

    Args:
        text (str): The text to be written to the file.
        file_path (str): The path to the file to be written.
    """
    with open(file_path, 'w') as file:
        file.write(text)


def write_text_to_file_with_pandas(text, file_path):
    """Function to write text to a file using pandas library.

    Args:
        text (str): The text to be written to the file.
        file_path (str): The path to the file to be written.
    """
    df = pd.DataFrame({'Text': [text]})
    df.to_csv(file_path, index=False)