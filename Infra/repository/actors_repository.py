from Infra.configs.connection import DBConnectionHandler
from Infra.entities.actors import Actors
from Infra.entities.films import Films

class Actorsrepository:
    def select(self):
        with DBConnectionHandler() as db:
            #data = db.session.query(Actors).all()
            data = db.session \
                .query(Actors) \
                .join(Films, Actors.film_title == Films.title) \
                .with_entities( 
                    Actors.name,
                    Films.genre,
                    Films.title
                ) \
                .all()
            return data