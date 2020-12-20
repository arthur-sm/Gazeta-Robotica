import atualizador as atualizador
import lib_handler.markov as markov


def main():
    escolha, demanda = 0, 0
    while(True):
        print('Escolha o que deseja fazer')
        print('0 - Atualizar banco de notícias e corrente de Markov')
        print('1 - Gerar notícias falsas')
        print('2 - Gerar notícias dentro de tópicos específicos')
        print('3 - Sair')
        escolha = int(input('Digite o número -> '))
        if(escolha == 0):
            print('Quantos tweets de cada conta devo raspar?')
            demanda = int(input('Digite o número -> '))
            atualizador.atualizarData(demanda)
        elif(escolha == 1):
            print('Quantas notícias falsas devo gerar?')
            demanda = int(input('Digite o número -> '))
            markov.gerar_frases(atualizador.paths.MARKOV_JSON, demanda)
        elif(escolha == 2):
            print(
                'Funcionalidade em andamento para ser implementada! Obrigado pela curiosidade ;)')
        elif(escolha == 3):
            print('Valeu!')
            break


if(__name__ == '__main__'):
    main()
