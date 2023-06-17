from flask import Flask, request, jsonify


app = Flask(__name__)


@app.route("/meow", methods=['POST'])
def meow():
    data = request.get_json()
    # Data pre-process if needed
    # call to the function from the main.py and pass parameters if needed
    # return the output of the function as a response to the frontend
    pass


if __name__ == '__main__':
    app.run(debug=True)
