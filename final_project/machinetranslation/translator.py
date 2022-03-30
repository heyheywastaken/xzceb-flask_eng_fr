import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
VERSION_LT='2022-03-28'

authenticator = IAMAuthenticator(apikey)
language_translator=LanguageTranslatorV3(version=VERSION_LT,authenticator=authenticator)
language_translator.set_service_url(url)


def english_to_french(english_text):
    text = language_translator.translate(text=english_text,model_id='en-fr').get_result()
    french_text=text['translations'][0]['translation']
    return french_text

def french_to_english(french_text):
    text = language_translator.translate(text=french_text,model_id='fr-en').get_result()
    english_text=text['translations'][0]['translation']
    return english_text

