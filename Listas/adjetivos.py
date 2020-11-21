#Acho que quanto mais adjetivos, melhor
from Auxiliares.aux_functions import contador

adjetivos_comum = [
#política
    'comunista',
    'de esquerda',
    'capitalista',
    'de direita',
    'liberal',
    'centrista',
    'burguês',
#pop
    'otaku',
    'gamer',
    'nerd',
    'indie',
    'conceitual',
    'gay',
#genérico
    'crente',
    'podre',
    'pobre',
    'popular',
    'adorável',
    'invisível',
    'rude',
    'agradável',
    'feliz',
    'alegre',
    'infeliz',
    'triste',
    'carente',
    'confiante',
    'indecente',
    'selvagem',
    'sensual',
    'excelente',
    'horrível',
    'inteligente',
    'pessimista',
    'otimista',
    'narcisista',
    'fiel',
    'infiel',
    'brega',
    'cafona',
    'incrível',
    'beneficente',
    'industrial',
    'natural',
    'fatal',
    'naturalista',
    'original',
    'profissional',
    'pirata'
]

adjetivos_raro = [
    'frio e calculista',
    'sem pé nem cabeça',
    'topper',
    'de cair o cu da bunda',
    'foda',
    'furry',
    'vegano',
    'cringe',
    'sem noção',
    'based',
    '[CENSURADO]',
    '[RAPAAAAAAIZ]'
]

def main():
    contador('Adjetivos', adjetivos_comum, adjetivos_raro)

if __name__ == '__main__':
    main()