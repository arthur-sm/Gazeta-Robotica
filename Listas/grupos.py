from Auxiliares.aux_functions import contador

grupo_comum = [
#Política
    'comunistas',
    'capitalistas',
    'liberais',
    'anarquistas',
    'centristas',
    'gados',
    'maçons',
    'burgueses',
#pop
    'armys',
    'otakus',
    'gamers',
    'bruxas',
    'boomers',
    'nerds',
    'youtubers',
    'influencers',
    'veganos',
    'E-girls',
    'indies',
    'caipiras',
    'maconheiros',
#empregos
    'jornalistas',
    'policiais',
    'padeiros',
    'artistas',
    'políticos',
    'empresários',
    'ladrões',
    'agricultores',
    'vagabundos',
    'programadores',
    'médicos',
    'professores',
    'comediantes',
    'poetas',
    'atletas',
    'filósofos',
    'militares',
    'astronautas',
#Outros
    'famílias'
]

grupo_raro = [
    'estudantes de medicina',
    'gays brancas',
    'robôs',
    'furrys',
    'farialimers',
    'gados',
    'piratas',
    '[CENSURADO]',
    '[RATINHÔÔÔ]'
]

def main():
    contador('Grupos', grupo_comum, grupo_raro)

if __name__ == '__main__':
    main()