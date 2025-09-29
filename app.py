from flask import Flask
from flask import Flask, abort, render_template, redirect, url_for, flash, request

app = Flask(__name__)


@app.route('/')
def home():  # put the application's code here
    return render_template('home.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/hobbies')
def hobbies():
    return render_template('hobbies.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/photography')
def photography():
    return render_template('photography.html')


if __name__ == '__main__':
    app.run()
