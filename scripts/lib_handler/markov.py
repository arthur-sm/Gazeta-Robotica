'''
    Conjunto de funções relacionadas à corrente de Markov (criar/armazenar/utilizar)

    Conteudo:
        class AbrirAquivo(object)
        def gerar_corrente(input: str, output: str)
        def gerar_frases(path: str, quantas: int)

    Componentes:
        Biblioteca Markovify
'''
import markovify


class AbrirAquivo(object):
    '''Classe utilizada em gerenciador de contexto para fechar documento automaticamente'''

    def __init__(self, filename: str, mode: str = 'r'):
        '''Abre o arquivo'''
        self.file = open(filename, mode, encoding="utf-8")

    def __enter__(self):
        '''Retorna conteudo do arquivo'''
        return self.file

    def __exit__(self, ctx_type, ctx_value, ctx_traceback):
        ''''Fecha arquivo'''
        self.file.close()


def gerar_corrente(input: str, output: str):
    '''Gera a corrente de Markov e chama a função _armazenar()

    Args:
        input: Path do arquivo que será lido.
        output: Path do arquivo para armazenar corrente de Markov.
    '''
    with AbrirAquivo(input) as f:
        matriz_markov = markovify.NewlineText(f.read(), state_size=3)
    print('    ☑ Corrente de Markov gerada')
    _armazenar(matriz_markov.to_json(), output)


def _armazenar(conteudo: str, path: str):
    '''Armazena corrente de Markov no arquivo especificado

    Args:
        conteudo: Aquilo que deve ser armazenado
        path: Path do arquivo para armazenar corrente de Markov.
    '''
    with AbrirAquivo(path, mode='w') as f:
        f.write(conteudo)
    print('Corrente de Markov armazenada ✔')


def carregar_corrente(path: str):
    with AbrirAquivo(path) as f:
        corrente_reconstruida = markovify.Text.from_json(f.read())
    return corrente_reconstruida

def gerar_frases(corrente, quantas: int) -> list:
    '''Gera frases baseadas na corrente de Markov fornecida e retorna elas em lista

    Args:
        path: Path do arquivo que contem a corrente de Markov.
        quantas: Quantidade de frases que devem ser geradas.
    '''
    frases = []
    while(quantas > 0):
        frases.append(corrente.make_short_sentence(280))
        quantas -= 1
    return frases