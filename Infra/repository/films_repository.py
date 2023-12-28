from Infra.configs.connection import DBConnectionHandler
from Infra.entities.films import Films
from sqlalchemy.orm.exc import NoResultFound
class Filmsrepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Films).all()
            return data

    def select_drama_films(self):
        with DBConnectionHandler() as db:
            try:
                data = db.session.query(Films).filter(Films.genre=="ggg").one() #Force execpt
                return data
            except NoResultFound:
                return None
            except Exception as exception:
                db.session.rollback() #Do rollback case exists a except!
                raise

    def insert(self, title, genre, year):
        with DBConnectionHandler() as db:
            try:
                data_insert = Films(title=title, genre=genre, year=year)
                db.session.add(data_insert)
                db.session.commit()
            except Exception as exception:
                db.session.rollback() #Do rollback case exists a except!
                raise

    def delete(self, title):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(Films.title==title).delete()
            db.session.commit()

    def update(self, genre, year):
        with DBConnectionHandler() as db:
            db.session.query(Films).filter(Films.genre == genre).update({"year":year})
            db.session.commit()