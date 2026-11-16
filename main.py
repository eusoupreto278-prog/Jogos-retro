from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/pong')
def pong():
    return render_template('pong.html')

@app.route('/snake')
def snake():
    return render_template('snake.html')

@app.route('/space_invaders')
def space():
    return render_template('space_invaders.html')

@app.route('/tetris')
def tetris():
    return render_template('tetris.html')

@app.route('/doom')
def doom():
    return render_template('doom.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)