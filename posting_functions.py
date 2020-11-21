'''
Código por ArthurSM
Gazeta Robótica
:)
'''

#Arquivo com todas as funções de opções de postagem para o BOT
#para organizar a adição

import random
from Listas.pessoas import pessoas_comum, pessoas_raro
from Listas.lugares import lugares_comum, lugares_raro
from Listas.substantivos import substantivos_comum, substantivos_raro
from Listas.adjetivos import adjetivos_comum, adjetivos_raro
from Listas.grupos import grupo_comum, grupo_raro
from Auxiliares.aux_functions import recebe_valor, evitar_repetir

RARO = 5
MEDIO = 12.5
COMUM = 20

def namoro_pp():
    #ATRIBUIÇÃO DE VALORES
    pessoa_a, pessoa_b = evitar_repetir(RARO, MEDIO, pessoas_raro, pessoas_comum)
    pessoa_a = pessoa_a.capitalize()
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = '{0} acaba de anunciar que está namorando com {1}'.format(pessoa_a, pessoa_b)
    elif(variedade == 2):
        imprima = '{0} e {1} assumem relacionamento estável e já falam até em casamento'.format(pessoa_a, pessoa_b)
    return imprima

def protesto_gsl():
    #ATRIBUIÇÃO DE VALORES
    grupo = recebe_valor(RARO, grupo_raro, grupo_comum).capitalize()
    substantivo = recebe_valor(MEDIO, substantivos_raro, substantivos_comum)
    lugar = recebe_valor(COMUM, lugares_raro, lugares_comum)
    variedade = random.randint(1,3)
    #FRASES
    if(variedade == 1):
        imprima = '{0} protestam contra {1} em {2}'.format(grupo, substantivo, lugar)
    elif(variedade == 2):
        imprima = 'Protestos contra {0} são feitos em {1} por {2}'.format(substantivo, lugar, grupo)
    elif(variedade == 3):
        imprima = '{0} de {1} protestam contra {2}'.format(grupo, lugar, substantivo)
    return imprima

def privatiza_s(): #mais uma ou duas variedades
    #ATRIBUIÇÃO DE VALORES
    substantivo = recebe_valor(COMUM, substantivos_raro, substantivos_comum)
    dinheiro = random.random()*1000
    variedade = random.randint(1,3)
    #FRASES
    if (variedade == 1):
        imprima = 'Min. da Economia Paulo Guedes fala em privatizar {0}: "Lucro de {1:.1f} bilhões"'.format(substantivo, dinheiro)
    elif (variedade == 2):
        imprima = 'Paulo Guedes planeja vender {0} à iniciativa privada'.format(substantivo)
    elif (variedade == 3):
        imprima = '"Se vendermos {0}, dá bilhão", diz Paulo Guedes'.format(substantivo)
    return imprima

def adoro_spl(): #tem potencial para mais uma variedade
    #ATRIBUIÇÃO DE VALORES
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    substantivo = recebe_valor(COMUM, substantivos_raro, substantivos_comum)
    lugar = recebe_valor(COMUM, lugares_raro, lugares_comum)
    variedade = random.randint(1,5)
    #FRASES
    if(variedade == 1):
        imprima = '"Adoro {0}", diz {1} antes de viajar para {2}'.format(substantivo, pessoa, lugar)
    elif(variedade == 2):
        imprima = '{0} admite não conseguir viver sem {1}'.format(pessoa, substantivo)
    elif(variedade == 3):
        imprima = '{0} admite ser grande fã de {1}'.format(pessoa, substantivo)
    elif(variedade == 4):
        imprima = '"O que seria do Brasil sem {0}?" questiona {1}'.format(substantivo, pessoa)
    elif(variedade == 5):
        imprima = '"O que diabos é {0}?", pergunta {1}'.format(substantivo, pessoa)
    return imprima

def album_psa():
    #ATRIBUIÇÃO DE VALORES
    pessoa = recebe_valor(MEDIO, pessoas_raro, pessoas_comum).capitalize()
    substantivo = recebe_valor(MEDIO, substantivos_raro, substantivos_comum)
    adjetivo = recebe_valor(RARO, adjetivos_raro, adjetivos_comum)
    variedade = random.randint(1,3)
    #FRASES
    if(variedade == 1):
        imprima = '{0} acaba de anunciar novo projeto músical e seu primeiro álbum: "{1} {2}"'.format(pessoa, substantivo, adjetivo)
    elif(variedade == 2):
        imprima = '"{0}" é o novo álbum {1} de {2}'.format(substantivo, adjetivo, pessoa)
    elif(variedade == 3):
        imprima = '{0} lança primeiro álbum de novo projeto músical: "{1}"'.format(pessoa, adjetivo)
    return imprima

def proibe_s(): #Adicionar mais uma variedade
    #ATRIBUIÇÃO DE VALORES
    substantivo = recebe_valor(COMUM, substantivos_raro, substantivos_comum)
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = 'Bolsonaro fala em decreto para proibir {0}'.format(substantivo)
    elif(variedade == 2):
        imprima = 'Câmara aprova lei para regulamentar {0}'.format(substantivo)
    return imprima

def desabafo_p(): #adicionar mais variedades, deixar pelo menos umas 7 no total
    #ATRIBUIÇÃO DE VALORES
    pessoa = recebe_valor(MEDIO, pessoas_raro, pessoas_comum).title()
    asterisco_1 = random.randint(5,7) * "*" #Verbo
    asterisco_2 = random.randint(6,9) * "*" #Nome
    variedade = random.randint(1,5)
    #FRASES
    if(variedade == 1):
        imprima = '{0} faz desabafo misterioso no twitter: "Queria mesmo era {1} com o {2}"'.format(pessoa, asterisco_1, asterisco_2)
    elif(variedade == 2):
        imprima = 'Tweet misterioso de {0} choca a internet: "Queria {1} a {2}"'.format(pessoa, asterisco_1, asterisco_2)
    elif(variedade == 3):
        imprima = 'Em seu Twitter, {0} admite "saudade de {1}"'.format(pessoa, asterisco_1)
    elif(variedade == 4):
        imprima = '"Fariam o {0}?", pergunta {1}, "me: old que ***"'.format(asterisco_2, pessoa)
    elif(variedade == 5):
        imprima = '"Fariam a {0}?", pergunta {1}, "me: old que ***"'.format(asterisco_2, pessoa)
    return imprima

def musicafeat_psap():
    #ATRIBUIÇÃO DE VALORES
    pessoa_a, pessoa_b = evitar_repetir(RARO, MEDIO, pessoas_raro, pessoas_comum)
    pessoa_a = pessoa_a.capitalize()
    substantivo = recebe_valor(COMUM, substantivos_raro, substantivos_comum)
    adjetivo = recebe_valor(COMUM, adjetivos_raro, adjetivos_comum)
    variedade = random.randint(1,3)
    #FRASES
    if(variedade == 1):
        imprima = '{0} anuncia lançamento de nova música: "{1} {2} (feat. {3})"'.format(pessoa_a, substantivo, adjetivo, pessoa_b)
    elif(variedade == 2):
        imprima = 'Nova música de {0} em parceria com {1} vai se chamar "{2} {3}"'.format(pessoa_a, pessoa_b, substantivo, adjetivo)
    elif(variedade == 3):
        imprima = 'Lançamento de "{0}", nova música de {1} com participação de {2}, deve ocorrer no próximo mês'.format(adjetivo, pessoa_a, pessoa_b)
    return imprima

def fan_ppa():
    #ATRIBUIÇÃO DE VALORES  
    pessoa_a, pessoa_b = evitar_repetir(RARO, MEDIO, pessoas_raro, pessoas_comum)
    pessoa_a.title()
    adjetivo = recebe_valor(MEDIO, adjetivos_raro, adjetivos_comum)
    variedade = random.randint(1,5)
    #FRASES
    if(variedade == 1):
        imprima = '{0} se diz grande fã de {1}: "uma pessoa muito {2}"'.format(pessoa_a, pessoa_b, adjetivo)
    elif(variedade == 2):
        imprima = '"Admiro como {0} consegue ser tão {1}", diz {2}'.format(pessoa_b, adjetivo, pessoa_a)
    elif(variedade == 3):
        imprima = '"O esforço de {0} para ser tão {1} é impressionante", diz {2}'.format(pessoa_b, adjetivo, pessoa_a)
    elif(variedade == 4):
        imprima = '"Me esforço para ser um pouco mais {0} cada dia", admite {1} em entrevista'.format(adjetivo, pessoa_a)
    elif(variedade == 5):
        imprima = '"{0} é uma versão mais {1} de mim", diz {2}'.format(pessoa_a, adjetivo, pessoa_b)
    return imprima

def eleitor_ppp():
    #ATRIBUIÇÃO DE VALORES
    pessoa_a = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    pessoa_b, pessoa_c = evitar_repetir(RARO, COMUM, pessoas_raro, pessoas_comum)
    lugar = recebe_valor(RARO, lugares_raro, lugares_comum)
    variedade = random.randint(1,4)
    #Geração de valores aleatórios para as intenções de votos
    #multiplicação por números quebrados para tornar mais próximo da realidade
    chance_a = random.randint(25,50) * 0.71
    chance_b = random.randint(15,30) * 0.82
    chance_c = random.randint(1,15) * 0.93
    #FRASES
    if(variedade == 1):
        imprima = '{0} apoia candidatura de {1} para governo de {2} em 2022'.format(pessoa_b, pessoa_c, lugar)
    elif(variedade == 2):
        imprima = '{0} anuncia que vai se candidatar à presidência em 2022 e terá {1} como vice'.format(pessoa_b, pessoa_c)
    elif(variedade == 3):
        imprima = 'ELEIÇÕES 2022: {0} tem {1:.1f}% das intenções de votos, seguido de {2} com {3:.1f}% e {4} com {5:.1f}%'.format(pessoa_a, chance_a, pessoa_b, chance_b, pessoa_c, chance_c)
    elif(variedade == 4):
        imprima = 'Em possível segundo turno entre {0} e {1}, {2:.1f}% dos eleitores diz que desiste do Brasil'.format(pessoa_b, pessoa_c, chance_a)
    return imprima

def prefiro_aap():
    #ATRIBUIÇÃO DE VALORES
    adjetivo_a, adjetivo_b = evitar_repetir(COMUM, RARO, adjetivos_raro, adjetivos_comum)
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    variedade = random.randint(1,3)
    #FRASES
    if (variedade == 1):
        imprima = '{0} diz preferir ser {1} do que {2}'.format(pessoa, adjetivo_a, adjetivo_b)
    elif (variedade == 2):
        imprima = '"Tem muita gente {0} hoje em dia, precisamos de mais gente {1}", diz {2}'.format(adjetivo_b, adjetivo_a, pessoa)
    elif (variedade == 3):
        imprima = 'OPINIÃO: {0} pode ser a inspiração que o povo precisa para ser menos {1} e mais {2}'.format(pessoa, adjetivo_b, adjetivo_a)
    return imprima

def estaciona_pl():
    #ATRIBUIÇÃO DE VALORES
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    lugar = recebe_valor(MEDIO, lugares_raro, lugares_comum)
    variedade = random.randint(1,2)
    #FRASES
    if (variedade == 1):
        imprima = '{0} estaciona carro em {1}'.format(pessoa, lugar)
    elif (variedade == 2):
        imprima = 'Saiba tudo sobre a mudança de {0} para {1}'.format(pessoa, lugar)
    return imprima

def comparar_ss():
    #ATRIBUIÇÃO DE VALORES
    substantivo_a, substantivo_b = evitar_repetir(MEDIO, RARO, substantivos_raro, substantivos_comum)
    variedade = random.randint(1,4)
    #FRASES
    if (variedade == 1):
        imprima = 'DICA DO DIA: Não trate como {0} quem te trata como {1}'.format(substantivo_a, substantivo_b)
    elif (variedade == 2):
        imprima = 'ARTIGO: "Por que {0} é uma coisa tão supervalorizada?"'.format(substantivo_a)
    elif (variedade == 3):
        imprima = 'OPINIÃO: "Quando {0} se tornou algo tão desvalorizado?"'.format(substantivo_a)
    elif (variedade == 4):
        imprima = 'OPINIÃO: Precisamos de mais {0} e menos {1}'.format(substantivo_a, substantivo_b)
    return imprima

def largo_psl():
    #ATRIBUIÇÃO DE VALORES
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    substantivo = recebe_valor(COMUM, substantivos_raro, substantivos_comum)
    lugar = recebe_valor(RARO, lugares_raro, lugares_comum)
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = '"Quero largar tudo e ir vender {0} em {1}", diz {2}'.format(substantivo, lugar, pessoa)
    elif(variedade == 2):
        imprima = '{0} quer "desistir de tudo" para vender {1} em {2}'.format(pessoa, substantivo, lugar)
    elif(variedade == 3):
        imprima = 'Bateu a vontade de jogar tudo pro alto e ir vender {0} na praia? Saiba o que fazer'.format(substantivo)
    return imprima

def paiva_p():
    #Atribuição de valores
    pessoa = 'uma das meninas do Anavitória (sei lá o nome delas kkkk)' #evitando esse termo da lista 'pessoas' em específico porque ela ultrapassa o limite de caracteres do twitter. Veja o último item da lista de afazeres.
    while (pessoa == 'uma das meninas do Anavitória (sei lá o nome delas kkkk)'):
        pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    #FRASES
    #twitter pediu pra diminuir o tamanho da frase :<
    imprima = 'Sabias que... A lenda {0}™ não dispensa de fumar uns bons canhões? \nSim, erva, marijuana. Droga. \nPara contemplar os árduos treinos, {0}, que quase também se pode chamar de Mestre dos Paivas, chupa fumo de uns bons tarolos para lidar com a pressão.'.format(pessoa)
    return imprima

def obras_ppsa():
    #Atribução de valores
    pessoa_a, pessoa_b = evitar_repetir(RARO, RARO, pessoas_raro, pessoas_comum)
    substantivo = recebe_valor(RARO, substantivos_raro, substantivos_comum)
    adjetivo = recebe_valor(RARO, adjetivos_raro, adjetivos_comum)
    variedade = random.randint(1,3)
    #FRASES
    if(variedade == 1):
        imprima = 'Globo anuncia nova novela "{0} {1}", estreando {2} como personagem principal e {3} como antagonista'.format(substantivo, adjetivo, pessoa_a, pessoa_b)
    elif(variedade == 2):
        imprima = '"{0}" é o novo livro de {1} que fala sobre {2}'.format(adjetivo, pessoa_a, substantivo)
    elif(variedade == 3):
        imprima = 'Em entrevista, {0} tenta resumir {1} em duas palavras: "{2} {3}"'.format(pessoa_a, pessoa_b, substantivo, adjetivo)
    return imprima

def time_p():
    #Atribução de valores
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    variedade = random.randint(1,4)
    #FRASES
    if(variedade == 1):
        imprima = '{0} é nova aposta do Flamengo para virar o jogo'.format(pessoa)
    elif(variedade == 2):
        imprima = '{0} recebe proposta do Vasco para jogar na próxima partida decisiva'.format(pessoa)
    elif(variedade == 3):
        imprima = 'Grêmio contrata {0} como líder do time e preve disparo na pontuação'.format(pessoa)
    elif(variedade == 4):
        imprima = 'Próximo da Zona de Rebaixamento, Corínthias toma medidas desesperadas e contrata {0}'.format(pessoa)
    return imprima

def trafico_ps():
    #Atribução de valores
    pessoa = recebe_valor(RARO, pessoas_comum,  pessoas_raro)
    substantivo = recebe_valor(MEDIO, substantivos_comum, substantivos_raro)
    ton = random.randint(2,50)
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = 'Policiais levam {0} para delegacia, prisão se dá por tráfico de {1}'.format(pessoa, substantivo)
    elif(variedade == 2):
        imprima = '{0} tenta traficar {1} toneladas de {2} e acaba na prisão'.format(pessoa, ton, substantivo)
    return imprima

def dia_do_a():
    #Atribução de valores
    adjetivo = recebe_valor(MEDIO, adjetivos_raro, adjetivos_comum)
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = 'Você sabia? Hoje é dia do cidadão {0}!'.format(adjetivo)
    elif(variedade == 2):
        imprima = 'Saiba qual presentes comprar para seu parente {0} preferido'.format(adjetivo)
    return imprima

def nessa_data_gg():
    #Atribuição de valores
    grupo_a, grupo_b = evitar_repetir(RARO,RARO, grupo_raro, grupo_comum)
    dia = random.randint(1,30)
    mes = random.randint(1,12)
    ano = random.randint(300, 2010)
    variedade = random.randint(1,5)
    #FRASES
    if(variedade == 1):
        imprima = 'Você sabia? Na data de hoje, {0} anos atrás, {1} adquiriram o direito de votar!'.format(ano, grupo_a)
    elif(variedade == 2):
        imprima = 'Hoje na história: em {0}, {1} realizavam um protesto massivo contra {2}'.format(ano, grupo_a, grupo_b)
    elif(variedade == 3):
        imprima = 'Curiosidade: em {0}/{1}/{2}, {3} de todo o mundo lutavam contra {4}'.format(dia, mes, ano, grupo_a, grupo_b)
    elif(variedade == 4):
        imprima = 'Estudos indicam que primeiros {0} podem ter surgido em cerca de {1} A.C.'.format(grupo_b, ano)
    elif(variedade == 5):
        imprima = 'Nova teoria da conspiração diz que {0} controlam o mundo'.format(grupo_a)
    return imprima

def show_pl():
    #Atribuição de valores
    pessoa = recebe_valor(RARO, pessoas_raro, pessoas_comum)
    lugar = recebe_valor(RARO, lugares_raro, lugares_comum)
    variedade = random.randint(1,2)
    #FRASES
    if(variedade == 1):
        imprima = '{0} anuncia show em {1}'.format(pessoa, lugar)
    elif(variedade == 2):
        imprima = 'Governo de {0} anuncia apresentação inédita de {1}'.format(lugar, pessoa)
    return imprima
    