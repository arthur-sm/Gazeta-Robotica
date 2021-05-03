'''Módulo focado em gerar frases e filtrar elas'''

import lib_handler.markov as markov
import paths


def gerar(qntd, topicos=None, censuras=None):
    '''Gera frases e filtra elas se necessário'''
    chamadas = []
    # Prepara a corrente de markov para se usada nas operações seguintes. Mais efetivo do que ter que carregar ela toda vez
    corrente = markov.carregar_corrente(paths.MARKOV_JSON)
    while len(chamadas) < qntd:
        # gera quantas notícias faltam para chegar à quantidade desejada
        noticias = markov.gerar_frases(corrente, qntd - len(chamadas))
        # Filta notícias que não estão dento dos tópicos
        if(topicos is not None):
            noticias = temas(noticias, topicos, True)
        # Filta notícias que contenham palavras banidas
        if(censuras is not None):
            noticias = temas(noticias, censuras, False)
        chamadas += noticias
    for elem in chamadas:
        print('-> {0}\n'.format(elem))


# Baseado no código de Brienna Herold
def temas(frases: list or tuple, topicos: list or tuple, pertence: bool):
    '''
    Recebe uma lista de frases e tópicos, retorna frases que contenham palavras da lista de tópicos

    args:
        frases -> Lista de frases para serem filtradas

        topicos -> Lista de palavras consideras tópicos desejados/censurados

        pertence -> Valor que indica se as frases devem ter os tópicos (True) ou não (False)
    '''
    saida = []
    assuntos = topicos.split(' ')
    for frase in frases:
        # Se uma das palavras dentro da frase estiver dentro dos assuntos
        no_assunto = bool([palavra for palavra in frase.split(
            ' ') if palavra.lower() in assuntos])
        if(no_assunto == pertence):
            saida.append(frase)
    return saida
