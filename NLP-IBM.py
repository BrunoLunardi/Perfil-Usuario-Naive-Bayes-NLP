# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 19:51:59 2021

@author: bruno
"""

#https://medium.com/analytics-vidhya/getting-started-with-notebooks-in-ibm-watson-nlu-part-1-3b0b92894901
#https://dataplatform.cloud.ibm.com/analytics/notebooks/v2/e61d0855-16bb-4211-85a8-17d8688a7148/view?access_token=11c481d4c8bbb8dd2fd1bc1830da23ceb407d8403324f270388fad4afa1c9cd8

################################## Importações para trabalhar com watson IBM ##################################
import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, EmotionOptions, SentimentOptions, KeywordsOptions

# from botocore.client import Config
# import ibm_boto3

################################## Importações ##################################
# import types 
import pandas as pd


################################## Configurações serviço IBM ##################################
#realiza autenticação com servidor IBM
authenticator = IAMAuthenticator('LsRvjTiGO2hm5CmMOkYumONXX1x08ej0nZED2cRZYvqM')
service = NaturalLanguageUnderstandingV1(
    version='2020-08-01',
    authenticator=authenticator
)

# #seleciona o serviço de processamento de linguagem natural
service.set_service_url('https://api.us-south.natural-language-understanding.watson.cloud.ibm.com/instances/fe0885df-7c76-4192-9bc8-6c6d7ca836ae')




################################## INÍCIO FUNÇÕES ##################################

def sentiment_and_keyword(st,service=service):
    """
    Função para fazer requisição com o servidor IBM e obter keywords e sentimento do texto a ser analisado
    return: JSON com análises do texto informado
    """
    return (service.analyze(text=st,features=Features(keywords=KeywordsOptions(sentiment= True,emotion= True,limit= 3),sentiment=SentimentOptions())).get_result())
    


def sentiment_extractor(row_num):
    """
    Função para pegar o score do sentimento e colocar em uma nova coluna dataframe
    return: score do sentimento
    """    
    sentiment_scores=df2['sentiment_keyword_json'][row_num]['sentiment']['document']
    return sentiment_scores


def keyword_extractor(row_num):
    """
    Função para pegar o score do keyword e colocar em uma nova coluna dataframe
    return: score do keyword
    """        
    keyword_scores=[{df2['sentiment_keyword_json'][row_num]['keywords'][i]['text'] : df2['sentiment_keyword_json'][row_num]['keywords'][i]['sentiment']['score']} for i in range(0,len(df2['sentiment_keyword_json'][row_num]['keywords']))]
    return keyword_scores

################################## FIM FUNÇÕES ##################################

#leitura da base de dados
df_data_1 = pd.read_csv('tokenised_dataset.csv')
#print(df_data_1.head())

#copiar 10 dados para testes
df1 = df_data_1.head(10)
# print(df1)


# for col in df1.columns: 
#     print(col) 

df1['sentiment_keyword_json'] = df1.apply(lambda row : sentiment_and_keyword(str(row['sentences'])),axis = 1)

df2 = df1[['sentences','sentiment_keyword_json']]

print(df2.head())

df2['sentiment_score'] = df2.apply(lambda row : sentiment_extractor(row.name),axis = 1)
df2['keyword_score'] = df2.apply(lambda row : keyword_extractor(row.name),axis = 1)
df2

# #realiza requisição com servidor IBM (envida dados para ser classificado)
# response = natural_language_understanding.analyze(
#     text="I am happy",
#     features=Features(emotion=EmotionOptions())).get_result()

# print(json.dumps(response, indent=2))

# print(type(response))

# print(response)