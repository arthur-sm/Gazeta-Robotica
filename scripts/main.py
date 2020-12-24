import atualizador
import frases
import lib_handler.markov as markov


def noticias_falsas():
    topicos, censura = None, None
    print('Deseja incluir tópicos específicos? 1 - Sim | 2 - Não')
    if int(input('-> ')) == 1:
        topicos = str(
            input('Digite os tópicos (separados por espaço): ')).lower()
    print('Deseja censurar tópicos específicos? 1 - Sim | 2 - Não')
    if int(input('-> ')) == 1:
        censura = str(
            input('Digite os tópicos censuráveis (separados por espaço): ')).lower()
    demanda = int(input('Quantas frases devem ser geradas -> '))
    frases.gerar(demanda, topicos, censura)


def main():
    escolha, demanda = 0, 0
    while(True):
        print('Escolha o que deseja fazer')
        print('0 - Atualizar banco de notícias e corrente de Markov')
        print('1 - Gerar notícias falsas')
        print('2 - Sair')
        escolha = int(input('Digite o número -> '))
        if(escolha == 0):
            print('Quantos tweets de cada conta devo raspar?')
            demanda = int(input('-> '))
            atualizador.atualizar_dados(demanda)
        elif(escolha == 1):
            noticias_falsas()
        elif(escolha == 2):
            print('Valeu!')
            break


if(__name__ == '__main__'):
    main()
