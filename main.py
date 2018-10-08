from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/us-form")
def index():
    return render_template("form.html")


# Functions for validation.
def empty_value(x):
    if x:
        return True
    else:
        return False

def character_length(x):
    if len(x)>2 and len(x)<21:
        return True
    else:
        return False

def email_at_symbol(x):
    if x.count("@") == 1:
        return True
    else:
        return False

def email_period(x):
    if x.count(".") == 1:
        return True
    else:
        return False


@app.route("/signup", methods=["post"])
def user_signup():

# Create variable from the form input
    username = request.form["username"]
    password = request.form["password"]
    passwordv = request.form["passwordv"]
    email = request.form["email"]

# Create empty strings for the error messages
    username_error = ""
    password_error = ""
    passwordv_error = ""
    email_error = ""

    if not empty_value(username):
        username_error="Required field."

    if not character_length(username):
        username_error="Must be between 3 and 20 characters."

    else:
        if " " in username:
            username_error="Spaces not allowed!"

    if not empty_value(password):
        password_error="Required field."

    if not character_length(password):
        password_error="Must be between 3 and 20 characters."

    else:
        if " " in password:
            password_error="Spaces not allowed!"

    if passwordv != password:
        passwordv_error="Passwords do not match."

    if empty_value(email):
        if not character_length(email):
            email_error="Must be between 3 and 20 characters."

        elif not email_at_symbol(email):
            email_error="Must contain atleast one @ symbol."

        elif not email_period(email):
            email_error="Must contain one dot(.)"

        else:
            if " " in email:
                email_error="Spaces not allowed!"

    if not username_error and not password_error and not passwordv_error and not email_error:
        username = username
        return redirect('/welcome?username={0}'.format(username))

    else:
        return render_template("form.html", username_error=username_error, username=username, password_error=password_error, password=password, passwordv=passwordv, passwordv_error=passwordv_error, email_error=email_error, email=email)


@app.route("/welcome")
def valid_signup():
    username=request.args.get('username')
    return render_template("welcome.html", username=username)


app.run()

app.run()
