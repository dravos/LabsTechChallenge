from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def main():
    return render_template('index.html')

@app.route('/ds3532')
def me()
	return render_template('me.html')


if __name__ == '__main__':
    app.run()
