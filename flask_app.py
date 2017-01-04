from flask import Flask, render_template
import random

app = Flask(__name__)
@app.route('/')
def indexPage():
    print (1)
    return "Hello"
if __name__ == '__main__':
    app.debug=True
    app.run()
