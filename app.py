import guess_game
import currency_roulette_game
import memory_game
from input_validation import input_validation
# Welcome () function takes a person's name as input and displays a personalized welcome message
def welcome():
    username = input('Enter your name :')
    welcomeMessege = f'Hi {username} and welcome to the World of Games: The Epic Journey'
    print(welcomeMessege)


# start_play() function presents a list of available games to the user:
def start_play():
    startMessege = 'Please choose a game to play:'
    gameIndex = 1
    gamesList = {
        'Memory Game': '- a sequence of numbers will appear for 1 second and you have to guess it back.',
        'Guess Game': '- guess a number and see if you chose like the computer.',
        'Currency Roulette': '- try and guess the value of a random amount of USD in ILS'
    }
    print(startMessege)
    for game, gameDescription in gamesList.items():
        print(gameIndex, game, gameDescription)
        gameIndex += 1
    usrGameSelection = input('')
    usrGameDfficulty = '0'

    while not input_validation(usrGameSelection, len(gamesList)):
        usrGameSelection = input('Please choose a game to play:')
    usrGameSelection=int(usrGameSelection)
    while not input_validation(usrGameDfficulty,5):
        usrGameDfficulty = input('select a difficulty level between 1 and 5:')
    usrGameDfficulty=int(usrGameDfficulty)

    if usrGameSelection == 1 : memory_game.Play(usrGameDfficulty)
    if usrGameSelection == 2 : guess_game.Play(usrGameDfficulty)
    if usrGameSelection == 3 : currency_roulette_game.Play(usrGameDfficulty)



