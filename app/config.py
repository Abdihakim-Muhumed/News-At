class Config :
    '''config parent class'''
    pass

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
