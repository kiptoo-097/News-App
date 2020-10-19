from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return "Hey there!"





if __name__ == "__main__":
    app.run(debug=True)
    app.run