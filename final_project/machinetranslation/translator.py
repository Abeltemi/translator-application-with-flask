"""
This module Translate English Language into French Language and vise versa
"""

from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    """
    This function translate text from english to french.
    """
    #write the code here
    word = MyMemoryTranslator(source='en', target="fr")
    french_text = word.translate(english_text)
    return french_text


def french_to_english(french_text):
    """
    This function translates the french language into English.
    """
    #write the code here
    word = MyMemoryTranslator(source='fr', target="en")
    english_text = word.translate(french_text)
    return english_text
