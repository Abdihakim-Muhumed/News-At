class Article:
    '''Article class to define article objects'''
    all_articles=[]
    def __init__(self,title,author,description,link,image_url,published_time):
        ''' __init__ method to create Article objects'''
        self.title = title
        self.author = author
        self.description = description
        self.link = link
        self.image_url = image_url
        self.published_time = published_time

@classmethod
def save_article(cls,self):
    '''Article class method that saves an article into the all_articles list'''
    cls.all_articles.append(self)