'''
Código por ArthurSM
Gazeta Robótica
:)
'''

import tweepy
from keys import * #Keys e Tokens necessários para postar na conta automaticamente

def criar_objeto_API(): #Realiza verificação e cria variável com dados armazenados
    auth = tweepy.OAuthHandler(api_key, api_key_secret)
    auth.set_access_token(bot_acess_tk, bot_acess_tk_secret)
    return tweepy.API(auth)

def enviar_tweet(api_obj,tweet): #Posta tweets
    api_obj.update_status(tweet)