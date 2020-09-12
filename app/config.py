class Config :
    '''General config parent class'''
    source_api = 'https://newsapi.org/v2/sources?apiKey={}'
    articles_api = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

class ProdConfig(Config): 
    '''productio config  child class
        arg: 
            config: parent config class

        '''
    pass

class DevConfig(Config):
    '''Development configuration child class
    arg:
        Config: parent configurations class
        '''

    debug = True
