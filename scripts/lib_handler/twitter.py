'''
    Série de funções relacionadas ao twitter e uso da biblioteca tweepy

    Conteudo:
        def api_auth()
        def enviar_tweet(api_obj: object, tweet: str)
        def raspa_tweets(api_obj: object, conta: str, qntd: int)

    Componentes:
        Biblioteca tweepy
'''

import tweepy

# Keys e Tokens necessários para postar na conta automaticamente
__api_key = '#####'
__api_key_secret = '#####'
__bot_acess_tk = '#####'
__bot_acess_tk_secret = '#####'


def api_auth() -> object:
    '''Realiza autenticação no twitter e retorna objeto com dados armazenados'''
    auth = tweepy.OAuthHandler(__api_key, __api_key_secret)
    auth.set_access_token(__bot_acess_tk, __bot_acess_tk_secret)
    return tweepy.API(auth,
                      retry_count=3,  # Diante de algum erro, tentar novamente 3 vezes
                      retry_delay=10,  # Tempo de espera entre tentativas
                      timeout=60,  # Máximo de tempo esperando uma resposta do twitter
                      # Esperar o limite de requisições da API ser restaurado para fazer outras requisições
                      wait_on_rate_limit=True,
                      # Notificar quando o tweepy está esperando o tempo de requisições ser restaurado
                      wait_on_rate_limit_notify=True
                      )


def enviar_tweet(api_obj: object, tweet: str):
    '''
        Posta tweets

        Args:
            api_obj: objeto com autenticação do twitter que permite postagem.
            tweet: conteudo que formará o tweet.
        '''
    api_obj.update_status(tweet)


def raspa_tweets(api_obj: object, conta: str, qntd: int) -> 'lista de objetos':
    '''
        Retorna certa quantidade de tweets da conta desejada
        
        Args:
            api_obj -> Objeto com informações e autenticação da API do Twitter
            conta -> Conta específica da qual se deseja raspar dados
            qntd -> Quantos tweets devem ser obtidos

        Returns:
            lista de objetos
    '''
    # O tweet_mode = "extended" serve pra evitar que o texto dos tweets seja cortado pelo tweepy
    return tweepy.Cursor(api_obj.user_timeline, id=conta, tweet_mode="extended").items(qntd)
