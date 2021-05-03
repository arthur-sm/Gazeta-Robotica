'''
    Esse script capta notícias de perfis do twitter, formata e armazena elas numa database utilizada para gerar uma corrente de markov

    Componentes: 
    
        Biblioteca Time

    Componente das importações: 
        Bibliotecas re, 
        tweepy, 
        pandas,
        markovify
'''

# Bibliotecas
import time
#arquivos
import paths
# Funções próprias
# Funções relacionadas ao twitter (auth, postar tweet, raspar tweets)
import lib_handler.twitter as twitter
# Funções que formatam os tweets e excluem os indesejados
import lib_handler.formatar as formatar
# Funções que lidam com a database de notícias
import lib_handler.armazenamento as armazenamento
# Funções relacionadas à corrente de Markov para gerar notícias
import lib_handler.markov as markov


# Lista de portais da onde tiraremos notícias
portais = (  # tweepy ignora maiúsculas/minúsculas, então podemos escrever de forma que facilite nossa leitura
    # Grande Mídia
    'UOL',
    'Folha',
    'G1',
    'JornalOGlobo',
    'Estadao',
    'Veja',
    'Metropoles',
    'Exame',
    # Revistas
    'RevistaISTOE',
    'RevistaEpoca',
    'RevistaPiaui',
    # Portais de nichos
    'MDiscosQAmigos',  # Música
    'RollingStoneBR', # Música
    'Omelete',  # POP
    'NerdBunker',  # POP
    'OlharDigital',  # Tecnologia
    'MeioBit',  # Tecnologia
    'GEGlobo',  # Esporte
    # Jornais Menores
    'AgenciaPublica',
    'PonteJornalismo',
    'NexoJornal',
    'Poder360',
    # Mídia internacional
    'BBCBrasil',
    'TheInterceptBR',
    'CNNBrasil',
    'DiploBrasil',
    'ViceBrasil',
    'DW_Brasil',
    # Comédia
    'Sensacionalista'
)


def listarNoticias(api_obj: object, portais: tuple or list, qntd: int) -> list:
    """
        Chama a função raspar_noticias() para cada conta em portais

        Args:
            api_obj: Objeto criado pelo tweepy, necessário para realizar ações na API do twitter.
            portais: Lista contendo todas as contas de quais deve-se raspar tweets.
            qntd: Quantos tweets devem ser raspados por conta.

        Returns:
            Lista de tweets formatados e a conta de onde cada um foi retirado.
    """
    lista_noticias = []  # Lista que vai receber todas as notícias e portais da onde saíram
    # Raspagem dos tweets
    print('Iniciando raspagem')
    for conta in portais:
        # O .append() é mais eficaz, mas por algum motivo ele não funciona aqui. Ainda estou estudando o porquê
        lista_noticias += (raspar_noticias(api_obj, conta, qntd))
        # Acompanhamento de quais portais já tiveram conteúdo raspado
        print(('    ☑ {0}').format(conta))
        # Pausa para evitar sobrecarga da API do twitter
        time.sleep(qntd * 0.01)
    print('Raspagem finalizada ✔')
    return lista_noticias


def raspar_noticias(api_obj: object, conta: str, qntd: int) -> list:
    """
        Raspa notícias do twitter e formata elas.

        Args:
            api_obj: Objeto criado pelo tweepy, necessário para realizar ações na API do twitter.
            conta: Conta do qual deve-se raspar os tweets.
            qntd: Quantos tweets devem ser raspados.

        Returns:
            Lista composta de elementos (conta, tweet da conta).
    """
    tweets_formatados, lista_tweets, lista_saida = [], [], []
    # Cria uma lista com o texto de cada tweet que não é uma reply
    lista_tweets = formatar.remove_replys(
        twitter.raspa_tweets(api_obj, conta, qntd))
    # Remove RT's e tweets vazios, além de formatar eles
    tweets_formatados = formatar.limpar_tweets(
        [tweet.full_text for tweet in lista_tweets])
    for tweet in tweets_formatados:  # Cria lista com notícia e da onde tiramos ela
        lista_saida.append((conta, tweet))
    return lista_saida


def atualizar_corrente(coluna: str, entrada: str, aux: str, saida: str):
    '''
        Utiliza dados do Dataframe para gerar uma Corrente de Markov e Armazenar ela\n

        Args:
            coluna: Nome da coluna do qual deve-se retirar os elementos em formato de lista
            entrada: Path do arquivo do dataframe (em .csv)
            aux: Path do arquivo onde os dados obtidos da coluna serão armazenados (em .txt)
            saida: Path do arquivo à receber conteudo da corrente de Markov (em .json)
    '''
    dados_coluna, dados_formatados = [], []
    # Obtem, em formato de lista, todos os dados da coluna especificada
    dados_coluna = armazenamento.retorna_dados(coluna, entrada)
    # Retira parênteses de todos os elementos da lista, pois são incompatíveis com o markovify
    dados_formatados = formatar.remove_parenteses(
        dados_coluna)
    # Escrevemos as chamadas num documento para que o markovify possa ler depois
    armazena_lista(dados_formatados, aux, 'w')
    # Markovify lê o documento gerado acima e cria a corrente
    markov.gerar_corrente(aux, saida)


def armazena_lista(lista: list or tuple, path: str, modo: str):
    '''
        Imprime cada elento da lista em um arquivo

        Args:
            lista: Conteudo a ser armazenado.
            path: Caminho do arquivo a ser modificado.
            modo: Argumento da função open() que determina como o documento será utilizado.
    '''
    # Modo 'a' = Adiciona novo conteúdo à lista
    # Modo 'w' = Escreve por cima do documento
    with markov.AbrirAquivo(path, mode=modo) as arquivo:
        for elem in lista:
            arquivo.write(elem)
            arquivo.write('\n')


def atualizar_dados(qntd: int = 500):
    '''
        Atualiza, em sequência, banco de notícias e corrente de markov.

        args:
            qntd: Quantos tweets devem ser obtidos.
    '''
    # Declaração de variáveis
    api_obj = twitter.api_auth()  # Criação do objeto API
    # Processamento
    armazenamento.atualizar_banco(listarNoticias(
        api_obj, portais, qntd), paths.NOTICIAS_CSV)
    atualizar_corrente('Chamada', paths.NOTICIAS_CSV, paths.CHAMADAS_TXT, paths.MARKOV_JSON)


if(__name__ == '__main__'):
    atualizar_dados()
