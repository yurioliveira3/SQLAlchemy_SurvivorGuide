#EXAMPLE 1:
# from Infra.repository.films_repository import Filmsrepository
# repo = Filmsrepository()
# repo.insert('someFilm_2', 'comedy', '1990')
# repo.delete('Scarface')
# data = repo.select()
# print(data)

#EXAMPLE 2:
#from Infra.repository.actors_repository import Actorsrepository
#act = Actorsrepository()
#data = act.select()
#print(data)

#EXAMPLE 3:
from Infra.repository.films_repository import Filmsrepository
from Infra.repository.actors_repository import Actorsrepository

flm = Filmsrepository()
act = Actorsrepository()

data_film = flm.select()

print(data_film)

data_0_film = flm.select()[0]

print(data_0_film.title)
print(data_0_film.actors)