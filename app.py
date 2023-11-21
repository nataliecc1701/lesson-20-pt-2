from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def show_form():
    '''Home page shows the madlibs beginning form'''
    return render_template("form.html")