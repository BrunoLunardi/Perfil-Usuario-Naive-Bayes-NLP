# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:51:59 2021

@author: bruno
"""

#https://medium.com/analytics-vidhya/getting-started-with-notebooks-in-ibm-watson-nlu-part-1-3b0b92894901
#https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/e61d0855-16bb-4211-85a8-17d8688a7148/view?access_token=11c481d4c8bbb8dd2fd1bc1830da23ceb407d8403324f270388fad4afa1c9cd8

import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions

#realiza autenticação com servidor IBM
authenticator = IAMAuthenticator('LsRvjTiGO2hm5CmMOkYumONXX1x08ej0nZED2cRZYvqM')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

#seleciona o serviço de processamento de linguagem natural
natural_language_understanding.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fe0885df-7c76-4192-9bc8-6c6d7ca836ae')

#realiza requisição com servidor IBM (envida dados para ser classificado)
response = natural_language_understanding.analyze(
    text="I am happy",
    features=Features(emotion=EmotionOptions())).get_result()

print(json.dumps(response, indent=2))

print(type(response))

print(response)