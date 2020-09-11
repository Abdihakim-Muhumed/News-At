from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page.
    '''
    return render_template('index.html')