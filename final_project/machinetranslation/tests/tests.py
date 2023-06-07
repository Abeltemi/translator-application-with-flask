import unittest

from translator import french_to_english, english_to_french

class EglishToFrenchTest(unittest.TestCase):
    
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()