from flask import Flask, render_template
# testing pycharm github
"""
To set up a virtual environment in the terminal enter;
# python -m venv [directory]

To activate virtual environment
# [directory]\\Scripts\\activate.bat

Set environment to development
# set FLASK_ENV=development

Set flask to run you main file
# set FLASK_APP=[python file]

then enter command 'flask run'
"""

# Create a Flask Instance
app = Flask(__name__)


# Create a route decorator
@app.route('/')
def index():
    first_name = 'Sam'
    stuff = "This is <strong>bold</strong> text"
    fave_pizza = ['Pepperoni', 'Cheese', 'Meat Feast', 24]
    return render_template('index.html',
                           first_name=first_name,
                           stuff=stuff,
                           fave_pizza=fave_pizza)


# localhost:5000/user/sam
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', user_name=name)


# Create custom error pages

# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500

# use 'set
