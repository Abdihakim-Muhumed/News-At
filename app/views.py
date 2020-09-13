from flask import render_template
from app import app
from .request import get_sources,get_articles

@app.route('/')
def index():
    '''
    View root page function that returns the index page.

    '''
    sources = get_sources()
    print(sources)
    return render_template('index.html', sources = sources)

@app.route('/source/<source_id>')
def source(source_id):
    '''function that displays all the articles of a source in source.html'''
    articles = get_articles(source_id)
    return render_template('source.html',source_id = source_id,articles = articles)
