import unittest
from app import print_name

class TestApp(unittest.TestCase):
    def test_print_name(self):
        self.assertEqual(print_name(),"hello world")
if __name__=='__main__':
    unittest.main()