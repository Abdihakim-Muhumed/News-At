class Config :
    '''General config parent class'''
    SOURCES_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'

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

    DEBUG = True
