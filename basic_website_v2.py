# basic_website.py
"""
Creates and hosts a basic website to demonstrate capabilities of flask and Python.
Content is basic information about Video Game console generations.

Will Feighner
2021 04 25
"""
import datetime

from flask import Flask, render_template

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


if __name__ == '__main__':
    app.run()
