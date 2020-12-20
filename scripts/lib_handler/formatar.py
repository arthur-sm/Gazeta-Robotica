'''
    Série de funções voltadas à formatação de textos
    
    Conteudo:
        def remove_replys(tweets: list or tuple)
        def remove_parenteses(strings: list or tuple)
        def limpar_tweets(tweets: list or tuple)

    Componentes:
        Biblioteca re (RegEx)
'''

import re


def _regras_noticias(lista_tweets: list or tuple) -> list:
    lista_saida = []
    for tweet in lista_tweets:
        lista_saida.append(
            re.sub(r"http\S+", "",  # Retira Links do tweet (http ou https)
                   re.sub(r"#\S+", "",  # Retira Hashtags
                          re.sub(r"RT", "",  # Retira 'RT' (caso sobre algum do remove_RT)
                                 re.sub(r"@\S+", "@insensoblog",  # Substitui as @ marcas pela do in-senso
                                        re.sub(r"&gt;", "",  # Retira esse caractere que vem nos tweets do Estadão
                                               tweet
                                               )
                                        )
                                 )
                          )
                   )
        )
    return lista_saida


def _removeRT(tweets: list or tuple) -> list:
    """Recebe uma lista de tweets e retorna uma lista sem tweets que incluam 'RT'"""
    return [tweet for tweet in tweets if bool(re.search('RT', tweet)) is False]


def _remove_vazio(tweets: list or tuple, min_caracteres: int) -> list:
    """
        Recebe uma lista de strings e remove aquelas que estão vazias ou são pequenas demais

        Args:
            tweets: lista de strings
            min_caracteres: número mínimo de caracteres que deve haver em cada string

        Returns:
            Lista de strings
    """
    return [tweet for tweet in tweets if len(tweet) > min_caracteres]


def remove_replys(tweets: list or tuple) -> list:
    '''Recebe uma lista de objetos tweets. Retorna aqueles que não são replys.'''
    # Utiliza propriedades do objeto para saber se o tweet é uma reply
    return [tweet for tweet in tweets if bool(tweet.in_reply_to_status_id) is False]


def remove_parenteses(strings: list or tuple) -> list:
    '''Recebe uma lista de strings e remove o parêntese de cada uma delas, mantendo o que estiver dentre eles'''
    lista_filtrada = []
    for string in strings:
        if(type(string) is str):
            lista_filtrada.append(re.sub('[()]', '', string))
    return lista_filtrada


def limpar_tweets(tweets: list or tuple) -> list:
    '''
        Executa várias funções que fazem uma faxina na lista de strings recebida

        Args:
            tweets: lista de tweets que devem ser formatada

        Returns:
            Lista de tweets formatados, sem RT's ou strings vazias
    '''

    # Declaração de variáveis
    rt_filtrado, noticias_formatadas, noticias_final = [], [], []
    # Processamento
    rt_filtrado = _removeRT(tweets)
    noticias_formatadas = _regras_noticias(rt_filtrado)
    noticias_final = _remove_vazio(noticias_formatadas, 15)
    return noticias_final
