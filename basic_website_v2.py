# basic_website.py
"""
Creates and hosts a basic website to demonstrate capabilities of flask and Python.
Content is basic information about Video Game console generations.

Will Feighner
2021 05 01
"""
import datetime
import string

from flask import Flask, render_template, flash
from passlib.hash import sha256_crypt

app = Flask(__name__)


def get_date_time():
    """Returns current local date and time"""
    return datetime.datetime.today().strftime("%m-%d-%Y %H:%M:%S")


@app.route('/')
def show_home():
    """Create and render Home page"""
    return render_template('home.html', datetime=get_date_time())


@app.route('/previous_generations/')
def show_previous():
    """Create and render previous generation console listings"""
    return render_template('previous.html')


@app.route('/8thgen/')
def show_8th_gen():
    """Create and render previous generation console listing"""
    return render_template('8thgen.html')


@app.route('/about/')
def show_about():
    """Create and render about info page"""
    return render_template('about.html')


@app.route('/register/')
def show_register():
    """Create and render register page"""
    return render_template('register.html')


@app.route('/login/')
def show_login():
    """Create and render login page"""
    return render_template('login.html')


def check_pass():
    """Checks hashed login password against user file hashed password"""
    # Input a test password
    test_pass = "sdev300Key!2 "
    # Hash the password
    hash_pass = sha256_crypt.hash(test_pass)
    # View the encrypted password
    print(hash_pass)
    # Call verify to compare the two entries
    print(sha256_crypt.verify(test_pass, hash_pass))


def is_registered(username):
    """Checks if user is already registered"""
    with open('../static/pass_file.txt', "r") as pass_file:
        if username in pass_file:
            return True
        return False


def special_test(input_string, special_req):
    """Tests if given string has enough punctuation/special characters"""
    counter = 0

    # Counts how many punctuation characters in given string
    for char in input_string:
        if char in string.punctuation:
            counter += 1

    return counter >= special_req


def complexity(password):
    """Checks password complexity"""
    lower_case_req = 1
    upper_case_req = 1
    digit_count = 1
    special_count = 1
    length = 12

    if (len(password) >= length) and (sum(char.islower() for char in password) >= lower_case_req
                                      and sum(char.isupper() for char in password) >= upper_case_req
                                      and sum(char.isdigit() for char in password) >= digit_count
                                      and special_test(password, special_count)):
        return True
    return False


def register(username, password, real_name, email_address):
    """Registers user"""
    error = ''

    if not username:
        error = 'Please enter your Username.'
    elif not password:
        error = 'Please enter your Password.'
    elif not is_registered(username):
        error = 'You are already registered'
    elif not complexity(password):
        error = 'Make your password more complex'

    if error == '':
        flash(error)

    with open('../static/pass_file.txt', "a") as pass_file:
        pass_file.writelines(username + " " + sha256_crypt.hash(password) + " " + real_name + " " +
                             email_address)


if __name__ == '__main__':
    app.run()
