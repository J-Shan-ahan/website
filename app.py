from flask import Flask, render_template, redirect, flash, request

app = Flask(__name__)
app.secret_key = 'bumblebee'


@app.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
