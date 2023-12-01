import os

# SCORES_FILE_NAME - A string representing a file name. By default “Scores.txt” :
SCORES_FILE_NAME = "Scores.txt"
# BAD_RETURN_CODE - A number representing a bad return code for a function.
# Screen_cleaner - A function to clear the screen (useful when playing memory game or before a new game starts).
def Screen_cleaner():
    # posix is os name for Linux or mac
    if os.name == 'posix':
        os.system('clear')
    # else screen will be cleared for windows
    else:
        os.system('cls')