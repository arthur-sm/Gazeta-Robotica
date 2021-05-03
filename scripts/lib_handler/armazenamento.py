'''
    Série de funções voltadas à manipulação e armazenamento de dataframes através da biblioteca pandas

    Conteudo:
        def atualizar_banco(noticias_novas: list, path: str)
        def retorna_dados(coluna: str, path: str)

    Componentes:
        Biblioteca pandas
'''

import pandas as pd


def atualizar_banco(noticias_novas: list, path: str):
    '''
        Carrega dataframe à partir do arquivo fornecido, adiciona notícias novas e armazena novamente

        Args:
            noticias_novas: lista de notícias que ainda devem ser armazenadas no dataframe
            path: caminho do arquivo onde o dataframe está armazenado (.csv)
    '''
    # Declaração de variáveis
    # DataFrame à ser atualizado e DataFrame com novos valores
    banco_noticias, novasNoticias = [], []
    # Dataframe baseado no que já está amarzenado com as atualizações e sua versão final, com possíveis duplicatas removidas
    bancoAtualizado, bancoFinal = [], []
    # Processamento
    # Recupera DataFrame armazenado no .csv sem o index
    banco_noticias = pd.read_csv(path, index_col=0, nrows=2800) 
    #limitando o número de notícias para diminuir armazenamento e tamanho do arquivo
    print("    ☑ DataFrame recuperado")
    # Novo DataFrame à partir de novas notícias coletadas
    novasNoticias = pd.DataFrame(
        data=noticias_novas, columns=['Portal', 'Chamada'])
    # Adicionamos os dados do novo DataFrame ao DataFrame antigo para atualizar ele
    bancoAtualizado = banco_noticias.append(novasNoticias, ignore_index=True)
    print("    ☑ Novas noticias adicionadas ao DataFrame")
    # Excluímos qualquer notícia duplicada que possa ter sido armazenada, mantendo a mais recentes (útil para atualizações de regras no banco)
    bancoFinal = bancoAtualizado.drop_duplicates(
        subset=['Chamada'], keep='last')
    # Armazenamos o DataFrame, agora devidamente atualizado, limpo de duplicatas e indexado num arquivo csv
    bancoFinal.to_csv(path_or_buf=path)
    print('DataFrame Armazenado ✔')


# Retorna todos os dados armazenados na coluna específicada como uma lista
def retorna_dados(coluna: str, path: str) -> list:
    '''
        Retorna lista contendo dados da coluna especificada

        Args:
            coluna: de qual coluna os dados devem ser retirados
            path: caminho do arquivo que guarda o dataframe (.csv)
    '''
    return ((pd.read_csv(path).reset_index(drop=True))[coluna]).tolist()
