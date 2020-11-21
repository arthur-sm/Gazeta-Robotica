'''
Código por ArthurSM
Gazeta Robótica
:)
'''

import random
import time
#Opções de postagem----------------------
from posting_functions import *
#Funções Auxiliares para as postagens
from Auxiliares.aux_functions import escolher_aleatorio, organizar_lista, criar_lista, get_time
#Realização da postagem com Tweepy
from Auxiliares.twitter_handler import criar_objeto_API, enviar_tweet

ESCOLHAS = 21 #Possibilidades de frases

#Define aleatoriamente qual vai ser o post
def main():
    #Variável com resultado final
    noticia = "Null"
    #Define quais posts são considerados repetidos e qual a chance de serem postados novamente
    noticias_recentes = criar_lista(ESCOLHAS)
    twitter_API = criar_objeto_API()
    escolha_frase = 0
    #"Como assim Python não tem Switch Case?"
    #Processamento
    while(True):
        tempo = get_time() #hora em que o processo de seleção inicia
        escolha_frase = escolher_aleatorio(noticias_recentes, ESCOLHAS) #Seleciona opção
        noticias_recentes = organizar_lista(noticias_recentes, escolha_frase) #Dificulta repostagem
        if(escolha_frase == 1):
            noticia = namoro_pp()
        elif(escolha_frase == 2):
            noticia = protesto_gsl()
        elif(escolha_frase == 3):
            noticia = privatiza_s()
        elif(escolha_frase == 4):
            noticia = adoro_spl()
        elif(escolha_frase == 5):
            noticia = album_psa()
        elif(escolha_frase == 6):
            noticia = proibe_s()
        elif(escolha_frase == 7):
            noticia = desabafo_p()
        elif(escolha_frase == 8):
            noticia = musicafeat_psap()
        elif(escolha_frase == 9):
            noticia = fan_ppa()
        elif(escolha_frase == 10):
            noticia = eleitor_ppp()
        elif(escolha_frase == 11):
            noticia = prefiro_aap()
        elif(escolha_frase == 12):
            noticia = estaciona_pl()
        elif(escolha_frase == 13):
            noticia = comparar_ss()
        elif(escolha_frase == 14):
            noticia = largo_psl()
        elif(escolha_frase == 15):
            noticia = paiva_p()
        elif(escolha_frase == 16):
            noticia = obras_ppsa()
        elif(escolha_frase == 17):
            noticia = time_p()
        elif(escolha_frase == 18):
            noticia = trafico_ps()
        elif(escolha_frase == 19):
            noticia = dia_do_a()
        elif(escolha_frase == 20):
            noticia = nessa_data_gg()
        elif(escolha_frase == 21):
            noticia = show_pl()
        enviar_tweet(twitter_API, noticia)
        print('Post enviado - {0}'.format(tempo))
        #print(noticia)
        time.sleep(1800)


if __name__ == "__main__":

  main()