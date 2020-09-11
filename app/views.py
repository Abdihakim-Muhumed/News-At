from flask import render_template
from app import app

@app.route('/')
def index():
    '''
    View root page function that returns the index page.
    '''
    return render_template('index.html')

@app.route('/source/<source_id>')

def source(source_id):
    '''function that returns a source and all the articles of that source'''
    return render_template('source.html',source_id = source_id)