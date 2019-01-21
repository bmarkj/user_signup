from flask import Flask, request, redirect, render_template
import cgi
import os

app = Flask(__name__)
app.config['DEBUG'] = True

#main request handler; loads page on initial browser request 
@app.route("/")
def index():
    return render_template('signup_form.html')


#functions to validate user input
def test_blank(field):
    if not field.strip() or field is None:
        return True

def test_length(field):
    if len(field) >= 3 and len(field) <= 20:
        return True

def test_space(field):
    if ' ' not in field:
        return True

def test_match(f1, f2):
    if f1 == f2:
        return True

def test_char(field):
    if "@" in field and "." in field:
        return True


#request handler to accept user input, test for validity and send response to browser
@app.route("/validate", methods=['POST'])
def validate():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify-password']
    email = request.form['email']

    usr_err_msg = ''
    pwd_err_msg = ''
    ver_err_msg = ''
    eml_err_msg = ''

    #validate username
    if not test_blank(username):
        if test_length(username):
            if test_space(username):
                usr_err_msg = ''
                username = username
            else:
                usr_err_msg = "Username cannot contain spaces."
                username = ''
        else:
            usr_err_msg = "Username must be between 3 and 20 characters."
            username = ''
    else:
        usr_err_msg = "Username field is required."
           
    # #validate password
    if not test_blank(password):
        if test_length(password):
            if test_space(password):
                pwd_err_msg = ''
                password = password
            else:
                pwd_err_msg = "Password cannot contain spaces."
                password = ''
        else:
            pwd_err_msg = "Password must be between 3 and 30 characters."
            password = ''
    else:
        pwd_err_msg = "Password field is required."

    # #validate verify_password
    if test_match(password, verify_password):
        ver_err_msg = ''
        verify_password = verify_password
    else:
        ver_err_msg = "Invalid. Passwords do not match"
        password = ''
        verify_password = ''

    # #validate email
    if not test_blank(email):
        if test_length(email):
            if test_space(email):
                if test_char(email):
                    eml_err_msg = ''
                    email = email
                else:
                    eml_err_msg = "Email must contain both the '@' and '.' characters."
                    email = ''
            else:
                eml_err_msg = "Email cannot contain spaces."
                email = ''
        else:
            eml_err_msg = "Email must be between 3 and 30 characters."
            email = ''
    else:
        pass
   
    #direct output
    if not usr_err_msg and not pwd_err_msg and not ver_err_msg and not eml_err_msg:
        return render_template('welcome.html', name=username)
    else:
        return render_template('signup_form.html', 
        usr_err_msg=usr_err_msg,
        pwd_err_msg=pwd_err_msg,
        ver_err_msg=ver_err_msg,
        eml_err_msg=eml_err_msg,
        username=username,
        email=email)    


app.run()