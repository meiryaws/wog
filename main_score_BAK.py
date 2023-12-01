from flask import Flask, render_template
from utils import SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    return render_template('index.html', score=score)

@app.route('/error')
def error_message():
    return render_template('error.html')


if __name__ == '__main__':
    f=open(SCORES_FILE_NAME,'r')
    score =f.read()
    app.run()
