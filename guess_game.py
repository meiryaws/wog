from utils import Screen_cleaner
from Scores import add_score
import random
#Generates a random number between 1 and the specified difficulty,saving it as the secret_number.
_usrGameDfficulty=5

def Generate_number(_usrGameDfficulty):
    secret_number = random.randint(1, int(_usrGameDfficulty))
    #print (secret_number)
    return secret_number


def Get_guess_from_user():
    userGuesss = input("Guess a number")
    while not userGuesss.isnumeric():
        userGuesss=input(f'Please enter a valid number')
    userGuesss=int(userGuesss)
    return(userGuesss)

def Compare_results(_secret_number,_userGuess):
    if _secret_number==_userGuess:return True



def Play(_usrGameDfficulty):
    Screen_cleaner()
    # a=Generate_number(_usrGameDfficulty)
    # b=Get_guess_from_user()
    # print (str(Compare_results(a,b)))

    if Compare_results(Generate_number(_usrGameDfficulty), Get_guess_from_user()):
        print("Great guess")
        add_score(_usrGameDfficulty)
    else:
        print("Try next time ;)")



#Play(3)



