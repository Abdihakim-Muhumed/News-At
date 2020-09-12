from app import app
import urllib.request,json
from .models import source
Source = source.Source
#getting the key
api_key = app.config["MY_KEY"]

#getting the base url
source_base_url = app.config['SOURCES_URL']

def get_sources():
    '''function to get data from the api url
        returns:
            source_results : a list of dictionary containing Source objects
    '''
    get_source_url = source_base_url.format(api_key)
    with urllib.request.urlopen(get_source_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results =None
        if get_sources_response["sources"]:
            sources_results_list = get_sources_response["sources"]
            sources_results = process_results(sources_results_list)


    return sources_results

def process_results(sources_list):
    '''function to process results and create Source objects
        args:
            sources_list: a list of dictionaries
        returns:
            sources_results: list of Source objects
    '''
    sources_results = []

    for source in sources_list:
        id = source.get('id')
        name = source.get('name')
        description = source.get('description')

        source_object = Source(id,name,description)
        sources_results.append(source_object)

    
    return sources_results

