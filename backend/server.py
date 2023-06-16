from flask import Flask


app = Flask(__name__)


@app.route("/meow")
def meow():
    # call to the function from the main.py
    pass


if __name__ == '__main__':
    app.run(debug=True)
