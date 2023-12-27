from Infra.configs.base import Base
from sqlalchemy import Column, String, Integer

#Entities
class Films(Base): #Implements
    __tablename__ = "films"

    title = Column(String, primary_key=True)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self): #Like a Print
        return "Films [title={0}, year={1}]".format(self.title,self.year)
