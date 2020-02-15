from unittest import TestCase

class HelloTest(TestCase):
    def test_hello(self):
        self.assertTrue(1==1)

    def test_empty_list(self):
        self.assertFalse([])
        self.assertTrue(['hello'])
