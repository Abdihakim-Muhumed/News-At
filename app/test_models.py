import unittest
from models import source

Source = source.Source

class TestSource(unittest.TestCase):
    '''unittest class to test the behaviour of Source class'''
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
        source2.save_source()
        self.assertEqual(len(Source.all_sources),1)

    if __name__ == '__main__':
        unittest.main()