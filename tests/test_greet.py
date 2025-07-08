import unittest
from main import greet

class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Vrinda"),"Hello Vrinda")
if __name__=='__main__':
    unittest.main()
