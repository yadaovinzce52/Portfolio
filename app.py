from flask import Flask
from flask import Flask, abort, render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from datetime import datetime

app = Flask(__name__)
Bootstrap5(app)
curr_date = datetime.now().date()
curr_year = datetime.now().year


@app.route('/')
def home():  # put the application's code here
    skills_front = ['Bootstrap', 'JavaScript', 'HTML', 'CSS', 'jQuery']
    skills_back = ['Python', 'Java', 'PL/SQL', 'Microservices', 'Oracle Cloud Infrastructure', 'Oracle']
    skills_tools = ['Git', 'JetBrains IDEs', 'Microsoft Azure', 'Postman', 'Atlassian Products']
    skills_other = ['RESTful APIs', 'CI/CD Pipelines', 'Test-Driven Development', 'Cross-Device compatibility',
                    'Agile Development', 'Object-Oriented Programming', 'Data Structures', 'Algorithms', 'JSON']
    skills = {'Frontend': skills_front, 'Backend': skills_back, 'Tools': skills_tools, 'Other': skills_other}
    return render_template('home.html', skills=skills, curr_year=curr_year)


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/photography')
def photography():
    return render_template('photography.html')


if __name__ == '__main__':
    app.run()
