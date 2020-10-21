from flask import render_template,request,redirect,url_for
from ..requests import getSources, get_articles
from ..models import Source
from . import main

@main.route('/')
def index():
    
    news = getSources()

    title = 'Highlights'

    return render_template('index.html',title = title, news = news)


@main.route('/entertainment/')
def entertainment():
    
    entertainment = get_articles("entertainment")

    title = 'Entertainment'

    return render_template('allnews.html',title = title, entertainment = entertainment)





