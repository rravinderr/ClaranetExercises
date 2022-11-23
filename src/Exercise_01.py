"""
Write a python or bash script that takes
three parameters: two strings and a directory name,
and substitutes any occurrence of the first string with the second string for any **file** in the directory, recursively.
"""
import os


def replace_string(s, e, d):
    global str_to_replace; str_to_replace = s
    global new_string; new_string = e
    global dir_name; dir_name = d

    entries = os.listdir(dir_name)
    recursive_call(entries)


def recursive_call(entries):
    # exit condition
    if not entries:
        return
    else:
        file_name = entries.pop()
        new_file_name = file_name.replace(str_to_replace, new_string)
        if os.path.isfile(f"{dir_name}/{new_file_name}"):
            print(f"The file {dir_name}/{new_file_name} already exists")
        else:
            os.rename(f"{dir_name}/{file_name}", f"{dir_name}/{new_file_name}")
    return recursive_call(entries)


if __name__ == "__main__":

    directory = "../TestFolder"

    # (Un)Comment one or the other line accordingly (the second one is to revert changes)
    replace_string("Test", "Prova", directory)
    #   replace_string("Prova", "Test", directory)
