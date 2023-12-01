from utils import SCORES_FILE_NAME
import os



def add_score(difficulty):
    POINTS_OF_WINNING = (difficulty * 3) + 5
    score_file = open(SCORES_FILE_NAME, 'r+')
    if os.path.exists(SCORES_FILE_NAME): score = score_file.read()
    if score == '':
        score = POINTS_OF_WINNING
    else:
        score = int(score) + POINTS_OF_WINNING
    score_file.seek(0)
    score_file.truncate()
    score_file.write(str(score))
