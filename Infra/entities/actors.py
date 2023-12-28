from Infra.configs.base import Base
from sqlalchemy import Column, String, Integer, ForeignKey

#Entities
class Actors(Base): #Implements
    __tablename__ = "actors"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    film_title = Column(String, ForeignKey("films.title")) #PK to FILMS
    
    def __repr__(self): #Like a Print
        return "Actors [name={0}, film title={1}]".format(self.name,self.film_title)
