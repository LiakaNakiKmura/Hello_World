# coding:utf-8

import unittest


if __name__ == '__main__':
    import sys, os
    sys.path.append(os.path.abspath(os.path.join(
            os.path.dirname(__file__),os.pardir)))
    sys.path.append('..')
    sys.path.append('./src')
    import src.fuga 
    from src.fuga import Fuga
else:
    from fuga import Fuga

class HogeTest(unittest.TestCase):

    def setUp(self):
        print('setUp')

    def test_first(self):
        print('test_first')

    def test_fuga(self):
        fuga = Fuga()
        self.assertTrue(fuga.index())
        
    def test_fixed(self):
        self.assertFalse(False)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(HogeTest))
    return suite

if __name__ == '__main__':
    unittest.main()