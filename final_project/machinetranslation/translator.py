import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator(apikey)
version_id = '2018-05-01'
language_translator = LanguageTranslatorV3(version=version_id,authenticator=authenticator)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    '''Takes english text as arguement and returns french translation'''
    translation_response = language_translator.translate(text=englishText, model_id='en-fr')
    translation = translation_response.get_result()
    frenchText = translation['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    '''Takes french text as arguement and returns english translation'''
    translation_response = language_translator.translate(text=frenchText, model_id='fr-en')
    translation = translation_response.get_result()
    englishText = translation['translations'][0]['translation']
    return englishText
