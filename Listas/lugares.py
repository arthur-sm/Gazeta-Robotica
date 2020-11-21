#Não é preciso adicionar tanta coisa uma vez que a lista de Estados se encaixa bem
from Auxiliares.aux_functions import contador

lugares_comum = [
#Estados (gist do Thiago F. Macedo no github, alterado)
    'Acre',
    'Alagoas',
    'Amapá',
    'Amazonas',
    'Bahia',
    'Ceará',
    'Distrito Federal',
    'Espírito Santo',
    'Goiás',
    'Maranhão',
    'Mato Grosso',
    'Mato Grosso do Sul',
    'Minas Gerais',
    'Pará',
    'Paraíba',
    'Paraná',
    'Pernambuco',
    'Piauí',
    'Rio de Janeiro',
    'Rio Grande do Norte',
    'Rio Grande do Sul',
    'Rondônia',
    'Roraima',
    'Santa Catarina',
    'São Paulo',
    'Sergipe',
    'Tocantins',
]

lugares_raro = [
    #genéricos
    'floresta',
    'igreja',
    'terreiro',
    'casa abandonada',
    'vulcão',
    'caverna',
    'praia',
    'palácio do planalto',
    'Cristo Redentor',
    'Macaranã',
    #outros
    'Nether',
    'Leblon',
    'rock in rio',
    'sua casa',
    'Hogwarts',
    'Narnia',
    'Madureiraaaaa láláiá',
    'ponte para Terabitia',
    'onde Judas bateu as botas',
    'onde é que tenha sol, é pra lá que eu vou',
]

def main():
    contador('Lugares', lugares_comum, lugares_raro)

if __name__ == '__main__':
    main()