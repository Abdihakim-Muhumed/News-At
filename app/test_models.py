import unittest
from models import source
from models import article

Source = source.Source

class TestSource(unittest.TestCase):
    ''' class to test the behaviour of Source class'''
    def setUp(self):
        '''Testcase method that runs before every other testcase method'''
        self.new_source = Source('abc-1','ABC News','ABC News is all here to enable you go through the world news updates.')

    def test__init__(self):
        '''Testcase method to test Source object is created'''
        source1 = Source('abc-1','ABC News','ABC News is all here to enable you go through the world news updates.')
        self.assertEqual(source1.id,'abc-1')
        self.assertEqual(source1.name,'ABC News')
        self.assertEqual(source1.description,'ABC News is all here to enable you go through the world news updates.')

    def test_save_source(self):
        '''Testcase method to test Source if object is saved'''
        source2= Source('abc-1','ABC News','ABC News is all here to enable you go through the world news updates.')
        source2.save_source(self)
        self.assertEqual(len(Source.all_sources),1)


class TestArticle(unittest.TestCase):
    '''Class to test the behaviour of Article class'''

    def setUp(self):
        '''Testcase method that runs before every other testcase method'''
        self.new_article = Article('Arsenal run riots','Soll Campell','Arsenal start off their Premeire league campaign with a comfortablewin against newly promoted side Fulham','www.skysport.com','skysport.com','2020-09-12T15:57:00Z')
    
    def test__init__(self):
        '''Testcase method to test if Article object is created correctly'''
        article1= Article('Arsenal run riots','Soll Campell','Arsenal start off their Premeire league campaign with a comfortablewin against newly promoted side Fulham','www.skysport.com','skysport.com','2020-09-12T15:57:00Z')
        self.assertEqual(article1.title,'Arsenal run riots')
        self.assertEqual(article1.author,'Soll Campell')
        self.assertEqual(article1.description,'Arsenal start off their Premeire league campaign with a comfortablewin against newly promoted side Fulham')
        self.assertEqual(article1.link,'www.skysport.com')
        self.assertEqual(article1.image_url,'skysport.com')
        self.assertEqual(article1.published_time,'2020-09-12T15:57:00Z')

    def test_save_source(self):
        '''Testcase method to test Article if object is saved'''
        article2= Article('Arsenal run riots','Soll Campell','Arsenal start off their Premeire league campaign with a comfortablewin against newly promoted side Fulham','www.skysport.com','skysport.com','2020-09-12T15:57:00Z')
        article2.save_article()
        self.assertEqual(len(Article.all_articles),1)


    if __name__ == '__main__':
        unittest.main()