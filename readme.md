# Gazeta Robótica [:robot:][:newspaper_roll:]

## O que é?
 Gazeta Robótica ([perfil no twitter](https://twitter.com/GazetaRobotica)) é um bot de twitter que gera notícias falsas à partir de notícias reais.
 Através da raspagem (ou scrapping) de tweets de portais de notícias, criamos um dataframe com milhares de chamadas reais (banco_noticias.csv) que são formatadas e utilizadas para criar uma corrente de Markov (Corrente_markov.json). Essa corrente, atualmente com uma ordem de 3, permite que criemos as notícias falsas.
 Nota: as # dos tweets são removidas para evitar que o bot saia por aí compartilhando hashtags aleatórias, o mesmo é feito com @ - que são substituidas por [@insensoblog](in-senso.com.br)

## Componentes
- ***Tweepy*** - Responsável por realizar o processo de autenticação, enviar tweets e raspar contas desejadas
- ***Time*** - Biblioteca utilizada para criar pausas entre raspagem de dados do twitter
- ***[Pandas](https://github.com/pandas-dev/pandas)*** - Biblioteca usada para criar, manipular e armazenar nosso dataframe de notícias
- ***Re*** - Utilizada para remover tweets que sejam rt's e formatar o restante para se encaixar nas regras necessárias
- ***[Markovify](https://github.com/jsvine/markovify)*** - Biblioteca que gera e armazena uma corrente de Markov à partir das notícias coletadas. Também cria as notícias falsas

## Como contribuir?
 Você pode contruir realizando algum dos afazeres na lista, corringindo erros de digitação, formatando o código, sugerindo melhoras ou aumentando a eficiência dos scripts.

### Lista de afazeres
#### Escopo Pequeno
- [ ] Adicionar opção de gerar notícias seguindo tópicos específicos (ou fora de tópicos específicos)
- [ ] Adicionar descrição para cada função e suas variáveis
- [ ] Fazer com que, cada vez que novas notícias sejam adicionadas no dataframe, o programa rearrange ele usando como categoria os portaias de notícia
- [ ] Adicionar tratamento de exceção nas devidas funções
#### Escopo Médio
- [ ] Gerenciar as contas que serão raspadas através de um documento, permitindo a remoção ou adição de mais perfis
- [ ] Criar sistema de feedback dos tweets, fazendo com que os tweets do bot com mais interação sejam adicionados no dataframe de notícias
### Escopo Grande
- [ ] Substituir o atual menu por um totalmente funcional, com boa aparência e mais opções

## Agradecimentos
- @marcelo-guimaraes, por ter dado a ideia para a versão 2.0 (tornar o bot baseado em scrapping + corrente de Markov)
- Todos que contribuiram com as bibliotecas utilizadas, bem como a linguagem em si

É nóis