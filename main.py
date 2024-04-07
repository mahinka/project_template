from app.io.input import *
from app.io.output import *

def main():
    file_path_builtin = "data/builtin.txt"
    file_path_pandas = "data/pandas.txt"

    text_from_console = input_text_from_console()
    output_text_to_console(text_from_console)

    write_text_to_file(text_from_console, file_path_builtin)
    text_file = read_text_from_file(file_path_builtin)
    output_text_to_console(text_file + " from built_in")

    write_text_to_file_with_pandas(text_from_console, file_path_pandas)
    text_file = read_text_from_file_with_pandas(file_path_pandas)
    output_text_to_console(text_file + " from pandas")


if __name__ == "__main__":
    main()