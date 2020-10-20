from app import app
import urllib.requests,json
from models import Source , Articles
import requests


api_key = None
source_url = None
article_url = None
base_url =None
base_article_url = None

def configure_request(app):
    global api_key,source_url,article_url, base_article_url,base_url
    api_key = app.config['NEWS_API_KEY']
    source_url = app.config['API_SOURCE_URL']
    base_article_url = app.config["ARTICLES_API_BASE_URL"]