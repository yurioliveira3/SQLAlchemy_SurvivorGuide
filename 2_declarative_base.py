from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

#Configs
eng = create_engine("postgresql+psycopg2://postgres:postgres@localhost:5432/cinema")
base = declarative_base()

#Vinculated session to the engine
session = sessionmaker(bind=eng)
ses = session()

#Entities
class films(base): #Implements
    __tablename__ = "films"

    title = Column(String, primary_key=True)
    genre = Column(String, nullable=False)
    year = Column(Integer, nullable=False)

    def __repr__(self): #Like a Print
        return "Films [title={0}, year={1}]".format(self.title,self.year)

#SQL

## SELECT ##
# Query to get all data from table films
data = ses.query(films).all() 
# Print all data
print(data)
# Print the title of the first element of array
print(data[0].title)
## SELECT ##

## INSERT ##
data_insert = films(title="Dracula", genre="Drama", year=1996)
ses.add(data_insert)
#ses.commit()
## INSERT ##

## DELETE ##
ses.query(films).filter(films.title=="Batman").delete()
#ses.commit()
## DELETE ##

## UPDATE ##
ses.query(films).filter(films.genre == "Drama").update({"year":2000})
## UPDATE ##

#DO COMMIT
ses.commit()

#CLOSE CONN
ses.close()