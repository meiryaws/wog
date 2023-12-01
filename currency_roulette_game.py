from update_currency import UpdateCurrency
from utils import Screen_cleaner
from Scores import add_score
import random

dollar_value = UpdateCurrency().convert(1, 'USD', 'ILS')
rand_number = random.randint(1, 100)


def get_money_interval(_usrGameDfficulty):
    interval = int(10 - int(_usrGameDfficulty))

    return interval


def Get_guess_from_user():
    userGuesss = input(f'Guess how much is {rand_number}$ in ILS : ')
    while not userGuesss.isnumeric():
        userGuesss = input(f'Please enter a valid number')
    userGuesss = int(userGuesss)
    return (userGuesss)


def Compare_results(_userGuess, interval):
    if rand_number * dollar_value - interval <= _userGuess <= rand_number * dollar_value + interval: return True


def Play(_usrGameDfficulty):
    UpdateCurrency()
    Screen_cleaner()
    if Compare_results(Get_guess_from_user(), get_money_interval(_usrGameDfficulty)):
        print("Great guess")
        add_score(_usrGameDfficulty)
    else:
        print(f'{rand_number}$ are {rand_number * dollar_value} in ILS . try next time')
