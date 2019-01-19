from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')

@app.route("/validate_signup", methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        username = request.form['username']


app.run()