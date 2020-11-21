'''
Código por ArthurSM
Gazeta Robótica
:)
'''

import random, time

#Em comentário -> DEBUG

def sortear_novamente(repeticoes): #Define a chance de ter que sortear novamente e realiza o teste
    DIFICULDADE = 10
    probabilidade = random.random() * 100
    if (probabilidade <= (DIFICULDADE/repeticoes)):
        output = False
    else:
        output = True
    print('Probabilidade = {0:.2f} | Chance = {1:.2f} | Repetições = {2} | Mudar = {3}'.format(probabilidade, DIFICULDADE/repeticoes, repeticoes, output))
    return output

def escolher_aleatorio(historico, limite): 
    #Escolhe um valor aleatório e verifica se esse valor já existe na lista (e em que quantidade)
    frase = random.randint(1,limite)
    print('lista -> {0} \nfrase: {1}'.format(historico, frase))
    num_iguais = 0
    for numero in historico:
        if(numero == frase): #há repetição?
            num_iguais += 1     #quantidade de repetições
    if(num_iguais > 0):
        if(sortear_novamente(num_iguais) == True):
            frase = escolher_aleatorio(historico, limite) #Recursividade para tornar a função mais eficaz
    return frase
    
def organizar_lista(lista, novo_elem):
    #Faz com que a lista "ande para frente", removendo o valor mais antigo e adicionando o novo
    lista.pop(len(lista) * -1)
    lista.append(novo_elem)
    return lista

def criar_lista(tamanho):
    #cria a lista com o tamanho desejado
    output = []
    i = 0
    while (i < tamanho):
        output.append(0)
        i += 1
    return output

def contador(palavras, array_comum, array_raro):
    qntd_comum = 0
    qntd_raro = 0
    for n in array_comum:
        qntd_comum += 1
    for n in array_raro:
        qntd_raro += 1
    total = qntd_comum + qntd_raro
    output = '{0} -> Qntd. Comum: {1} (Chance {2:.2f}%)| Qntd. Raro: {3} (Chance {4:.2f}%)| Qntd. Total: {5} ({6:.2f} raros para cada comum)'.format(palavras, qntd_comum, (100/qntd_comum), qntd_raro, (100/qntd_raro), total, (qntd_raro/qntd_comum))
    print(output)

def recebe_valor(probabilidade, array_raro, array_comum): 
    #Retorna valor aleatório de uma array ou outra
    #ATRIBUIÇÃO DE VALORES
    output = 'Null'
    chance = 0
    chance = random.random()*100
    #Processamento
    if (chance <= probabilidade):
        output = random.choice(array_raro)
    else:
        output = random.choice(array_comum)
    return output

def evitar_repetir(probabilidade_1, probabilidade_2, array_raro, array_comum): 
    #Executa receba_valor evitando repetição entre dois itens
    #ATRIBUIÇÃO DE VALORES
    pessoa_1, pessoa_2 = 'null', 'null'
    #Processamento
    while(pessoa_1 == pessoa_2):
        pessoa_1 = recebe_valor(probabilidade_1, array_raro, array_comum)
        pessoa_2 = recebe_valor(probabilidade_2, array_raro, array_comum)
    return pessoa_1, pessoa_2

def get_time():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    return current_time