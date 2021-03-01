# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:51:59 2021

@author: bruno
"""

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

authenticator = IAMAuthenticator('LsRvjTiGO2hm5CmMOkYumONXX1x08ej0nZED2cRZYvqM')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fe0885df-7c76-4192-9bc8-6c6d7ca836ae')

response = natural_language_understanding.analyze(
    text="I am happy",
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

print(type(response))