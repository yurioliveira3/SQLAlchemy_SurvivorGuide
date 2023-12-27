from Infra.configs.connection import DBConnectionHandler
from Infra.entities.films import Films

class Filmsrepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Films).all()
            return data

    def insert(self, title, genre, year):
        with DBConnectionHandler() as db:
            data_insert = Films(title=title, genre=genre, year=year)
            db.session.add(data_insert)
            db.session.commit()

    def delete(self, title):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(Films.title==title).delete()
            db.session.commit()

    def update(self, genre, year):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(Films.genre == genre).update({"year":year})
            db.session.commit()