from Infra.repository.films_repository import Filmsrepository

repo = Filmsrepository()

repo.insert('someFilm_2', 'comedy', '1990')

repo.delete('Scarface')

data = repo.select()

print(data)