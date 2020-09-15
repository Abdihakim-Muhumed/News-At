import urllib.request,json
from .models import Source, Article

#getting the key
api_key = None

#getting the base url
source_base_url = None
article_base_url = None
headlines_base_url = None

def configure_request(app):
    global api_key,source_base_url,article_base_url,headlines_base_url
    api_key = app.config['MY_KEY']
    source_base_url = app.config['SOURCES_URL']
    article_base_url = app.config["ARTICLES_URL"]
    headlines_base_url = app.config["HEADLINES_URL"]

def get_sources():
    '''function to get data from the api url
        returns:
            source_results : a list of dictionary containing Source objects
    '''
    get_sources_url = source_base_url.format(api_key)
    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results =None
        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_sources_results(sources_results_list)


    return sources_results

def process_sources_results(sources_list):
    '''function to process results and create Source objects
        args:
            sources_list: a list of dictionaries
        returns:
            sources_results: list of Source objects
    '''
    sources_results = []
    counter = 0
    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')

        source_object = Source(id,name,description)
        sources_results.append(source_object)

        counter +=1
        if counter == 15:
            break

    return sources_results

def get_articles(id):
    '''function to get all articles from a source and create article objects
        args:
            id: id of the source of which its articles are to be gotten
            
        returns:
            articles_results: a list of articles results
    '''
    get_articles_url = article_base_url.format(id,api_key)
    with urllib.request.urlopen(get_articles_url) as url:
        get_articles_data = url.read()
        get_articles_response = json.loads(get_articles_data)


        articles_results = None

        if get_articles_response["articles"]:
            articles_results_lists = get_articles_response["articles"]
            articles_results = process_articles_results(articles_results_lists)
        
    return articles_results


def get_headlines():
    '''function to get top headlines 
        returns:
            headlines_results:a list of top articles
        '''
    get_headlines_url = headlines_base_url.format(api_key)
    with urllib.request.urlopen(get_headlines_url) as url:
        get_headlines_data = url.read()
        get_headlines_response = json.loads(get_headlines_data)

        headlines_results = None

        if get_headlines_response["articles"]:
            headlines_results_lists = get_headlines_response["articles"]
            headlines_results = process_headlines_results(headlines_results_lists)
        
    return headlines_results

def process_headlines_results(headlines_list):
    ''' Function to process the results from get_headlines function
        args:
            headlines_list: alist of dictionaries from get_headlines function
        returns:
            articles_results: a list of Article objects'''        
    
    articles_results = []
    counter = 0
    for article in headlines_list:
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        link = article.get('url')
        image_url = article.get('urlToImage')
        published_time = article.get('publishedAt')
        article_object = Article(title,author,description,link,image_url,published_time)
        articles_results.append(article_object)
        counter +=1
        if counter == 4:
            break 

    return articles_results

def process_articles_results(articles_list):
    ''' Function to process the results from get_articles function
        args:
            articles_list: alist of dictionaries returned by get_articles function
        returns:
            articles_results: a list of Article objects'''        
    
    articles_results = []
    for article in articles_list:
        title = article.get('title')
        author = article.get('author')
        description = article.get('description')
        link = article.get('url')
        image_url = article.get('urlToImage')
        published_time = article.get('publishedAt')
        article_object = Article(title,author,description,link,image_url,published_time)
        articles_results.append(article_object)

    return articles_results


