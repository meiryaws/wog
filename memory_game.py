from utils import Screen_cleaner
from Scores import add_score
import os
import random
import sys
import time


def generate_sequence(_usrGameDfficulty):
    random_list = random.sample(range(1, 101), _usrGameDfficulty)
    print(random_list, end="")
    time.sleep(0.7)
    print("\r    ")

    return random_list


def get_list_from_user(_usrGameDfficulty):
    try:
        usr_list = list(int(num) for num in input(f'Enter the list of {_usrGameDfficulty} items separated by space . only {_usrGameDfficulty} first numbers will be recorded: ').strip().split())[:_usrGameDfficulty]
        return usr_list
    except:
        print("Error , you didnt enter list of numbers . lets try again...")
        Play(_usrGameDfficulty)


def is_list_equal(_usr_list, _random_list):
    if _usr_list == _random_list: return True

def Play(_usrGameDfficulty):
    Screen_cleaner()
    if is_list_equal(generate_sequence(_usrGameDfficulty), get_list_from_user(_usrGameDfficulty)):
        print("great")
        add_score(_usrGameDfficulty)
    else:
        print("Try Next Time ;)")

