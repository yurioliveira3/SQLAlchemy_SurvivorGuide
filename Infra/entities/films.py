from Infra.configs.base import Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

#Entities
class Films(Base): #Implements
    __tablename__ = "films"

    title = Column(String, primary_key=True)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    #Get all actors with relation between the returned film
    actors = relationship("Actors", backref="actors", lazy="subquery")

    def __repr__(self): #Like a Print
        return "Films [title={0}, year={1}]".format(self.title,self.year)
