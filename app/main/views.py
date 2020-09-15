from flask import render_template
from . import main
from ..request import get_sources,get_articles,get_headlines
from ..models import Source, Article

@main.route('/')
def index():
    '''
    View root page function that returns the index page.

    '''
    sources = get_sources()
    headlines = get_headlines()
    print(sources)
    print(headlines)
    return render_template('index.html', sources = sources,headlines = headlines)

@main.route('/source/<source_id>')
def source(source_id):
    '''function that displays all the articles of a source in source.html'''
    articles = get_articles(source_id)
    return render_template('source.html',source_id = source_id,articles = articles)

