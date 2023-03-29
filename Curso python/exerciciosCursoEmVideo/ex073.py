campeonato = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo', 'Athletico-PR','Atlético-MG', 'Fortaleza', 'São Paulo', 'América-MG', 'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba','Cuiabá', 'Ceará', 'Atlético-GO', 'Avaí', 'Juventude')
print(f"""
Os times classificados no Campeonato 
Brasileiro de Futebol são:
{sorted(campeonato)}
{'='*60}
Os cinco primeros classificados são:
{campeonato[:5]}
{'='*60}
Os quatro ultimos colocados são:
{campeonato[-4:]}
{'='*60}
O Corinthians ficou classificado na {campeonato.index('Corinthians') + 1}° colocação.

""")