class Source :
    '''source class to define source object'''
    all_sources = []
    def __init__(self,id,name,description,):
        '''__init__ method to instantiate source object'''
        self.id = id
        self.name = name
        self.description = description

    @classmethod
    def save_source(cls,self):
        '''method to save a class'''
        cls.all_sources.append(self)

    