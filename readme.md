# Gazeta Robótica [:robot:](emoji_rosto_robo)[:newspaper_roll:](emoji_jornal_enrolado)

## O que é?
 Gazeta Robótica ([perfil no twitter](https://twitter.com/GazetaRobotica)) é um bot de twitter que gera notícias aleatóriamente ao alocar termos/nomes específicos em frases pré-programadas.

## Componentes
- ***Tweepy*** - Responsável por realizar o processo de autenticação com a conta do bot e enviar tweets automaticamente
- ***Time*** - Biblioteca utilizada para criar pausas entre as postagens
- Muitas, muitas arrays...

## Como contribuir?

 Bom, estou criando esse repositório mais para manter o desenvolvimento organizado do que para esperar que alguém se interesse o suficiente para contribuir... Mas já que você tem interesse...
 O programa funciona através de dois eixos: as arrays (pessoas.py, lugares.py, etc...) e as frases pré-programadas (posting_functions.py). As primeiras existem em maior quantidade e dão o aspecto inusito às notícias, enquanto as frases tentam imitar um pouco os títulos de reportagens e coisas do tipo. Você também pode ajudar ao completar algo da lista de afazeres ou fazer outra melhora nos algoritmos e códigos do programa.

 ### Adicionando elementos nas listas
  Provavelmente a coisa mais fácil de se fazer aqui. Basta adicionar o que quiser entre parênteses e colocar a vírgula se não for o último argumento da array. Lembrando sempre de colocar na devida categoria (sinta-se livre para criar uma se achar que ajudaria a organizar o projeto). Antes de adicionar algo, lembre-se de pensar consigo mesmo:
   1. Isso poder ser ofensivo para alguma minoria?
   2. Isso é um assunto que pode/deve ser levado como brincadeira, e não algo que deve ser tratado com extrema seriedade?
   3. Isso pode violar as *Regras do Twitter*?

  Pensou e acha que o que você quer adicionar passa por todas essas perguntas tranquilamente? Ótimo! Já é meio caminho andado :)

### Adicionando novas frases
  Quando for adicionar uma nova função que usa uma nova frase, lembre-se de nomear ela com termos-chave e as inicias das listas que ela utiliza (p - pessoas, l - lugares, a - adjetivos, etc...). Depois basta incluir entre as possibilidades do posting.py e incrementar a constante **ESCOLHAS**.

### Lista de afazeres
- [x] Fazer a escolha da notícia sofrer influência da lista de escolhidas recentemente
- [ ] Colocar probabilidade de incluir tags como URGENTE, EXCLUSIVO, etc...
- [ ]  Adicionar possibilidade infíma de acionar a hashtag #philobot (1% ou menos, para não abusar do bot)
- [ ] Utilizar a biblioteca *Time* para imprimir o horário que o tweet foi enviado
- [ ] Mudar o algoritmo que dificulta repetição para ele ser baseado na posição das repetições na array ao invés da quantidade delas (Assim uma frase que acabou de ser escolhida tem menos chance de ser repostada do que uma que está no final da array)
- [ ] Adicionar tratamento de exceções para limite de caracteres do twitter
- [ ] Trocar cada elemento nas listas por um objeto com características como versões no singular/plural, masculino/feminino/neutro, etc... (Isso é viável? Ou melhor, compensa?)

Feito com [:zap:](emoji_raio_elétrico)