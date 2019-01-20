from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('signup_form.html')


def not_valid_blank(field):
    if field is None or field.strip():
        return True

def not_valid_length(field):
    if field.len() < 3 or field.len() > 20:
        return True

def not_valid_space(field):
    if ' ' in field:
        return True

def not_valid_match(f1, f2):
    if f1 != f2:
        return True

def not_valid_char(field):
    if "@" not in field or "." not in field:
        return True


@app.route("/validate-signup", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    usr_err_msg = ''
    pwd_err_msg = ''
    ver_pwd_err = ''
    eml_err_msg = ''

    #validate username
    if not_valid_blank(username):
        usr_err_msg = "Username field is required"
    elif not_valid_length(username):
        usr_err_msg = "Invalid. Must be between 3 and 20 characters."
    elif not_valid_space(username):
        usr_err_msg = "Invalid. Cannot contain spaces."

    #validate password
    if not_valid_blank(password):
        usr_err_msg = "Password field is required"
    elif not_valid_length(password):
        usr_err_msg = "Invalid. Must be between 3 and 20 characters."
    elif not_valid_space(password):
        usr_err_msg = "Invalid. Cannot contain spaces."

    #validate verify_password
    if not_valid_match(password, verify_password):
        ver_pwd_err = "Invalid. Passwords do not match"

    #validate email
    if  email is not None and email is not email.strip():
        if not_valid_length(email):
            eml_err_msg = "Invalid. Must be between 3 and 20 characters."
        elif not_valid_space(email):
            eml_err_msg = "Invalid. Cannot contain spaces."
        elif not_valid_char(email):
            eml_err_msg = 'Invalid. Must conatin both the "@" and "." characters.'

    return None
        
        
@app.route("/welcome")
def welcome():
    pass







app.run()