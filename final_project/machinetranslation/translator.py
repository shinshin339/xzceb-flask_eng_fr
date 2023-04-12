"""
translator.py: A module for translating text using the IBM Watson Language Translator API.
"""

import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
URL = os.getenv('URL')

authenticator = IAMAuthenticator(API_KEY)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(URL)

def english_to_french(english_text):
    """
    Translates English text to French.
    """
    french_text = language_translator.translate(
        text=english_text,
        model_id='en-fr'
    ).get_result()
    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    """
    Translates French text to English.
    """
    english_text = language_translator.translate(
        text=french_text,
        model_id='fr-en'
    ).get_result()
    return english_text['translations'][0]['translation']
