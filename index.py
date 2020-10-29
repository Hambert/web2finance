from flask import Flask


app = Flask(__name__)


@app.route('/')
def home():
    return 'Home Page Route'


if __name__ == '__main__':
    # running app
    app.run(use_reloader=True, debug=True)
