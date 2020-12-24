'''Módulo focado em gerar frases e filtrar elas'''

import lib_handler.markov as markov
import paths


def gerar(qntd, topicos=None, censuras=None):
    '''Gera frases e filtra elas se necessário'''
    chamadas = []
    # Prepara a corrente de markov para se usada nas operações seguintes. Mais efetivo do que ter que carregar ela toda vez
    corrente = markov.carregar_corrente(paths.MARKOV_JSON)
    while len(chamadas) < qntd:
        noticias = markov.gerar_frases(corrente, qntd)
        # Filta notícias que não estão dento dos tópicos
        if(topicos is not None):
            noticias = temas(noticias, topicos)
        # Filta notícias que contenham palavras banidas
        if(censuras is not None):
            noticias = censurar(noticias, censuras)
        chamadas += noticias
    for elem in chamadas:
        print('-> {0}\n'.format(elem))


def temas(frases, topicos):  # Baseado no código de Brienna Herold
    '''Recebe uma lista de frases e tópicos, retorna frases que contenham palavras da lista de tópicos'''
    saida = []
    assuntos = topicos.split(' ')
    for frase in frases:
        # Se uma das palavras dentro da frase estiver dentro dos assuntos
        no_assunto = bool([palavra for palavra in frase.split(
            ' ') if palavra.lower() in assuntos])
        if(no_assunto is True):
            saida.append(frase)
    return saida


def censurar(frases, censuras):
    '''Recebe uma lista de frases e palavras censuráveis, retorna frases que não contenham palavras censuráveis'''
    saida = []
    banidas = censuras.split(' ')
    for frase in frases:
        # Se uma das palavras dentro da frase estiver dentro das palavras banidas, não inclui ela na saída
        palavra_banida = bool(
            [palavra for palavra in frase.split(' ') if palavra.lower() in banidas])
        if (palavra_banida is not True):
            saida.append(frase)
    return saida
