from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from Infra.entities.films import Films
from unittest import mock
from .films_repository import Filmsrepository

# "VIRTUAL" DB
class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data=[
                #STUB DATA
                (
                    [mock.call.query(Films)],
                    [Films(title="Xau", genre="TTT", year=12)]
                ),
                (
                    [ #Acess Way
                        mock.call.query(Films),
                        mock.call.filter(Films.genre=="MMM")
                    ],
                    [
                        #Films(title="Hello", genre="MMM", year=12),
                        Films(title="Yuri", genre="MMM", year=14)
                    ]
                )
                #STUB DATA
            ]
        )

    #Always when enter in class, create session
    def __enter__(self): 
        return self #Return the context

    #Always when exit in class, close session
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()

#Test in select
def test_select(): #TEST CLASS, NEED BE PREFIX "test_"
    film_rep = Filmsrepository(ConnectionHandlerMock)
    resp = film_rep.select()
    print()
    print(resp)
    assert isinstance(resp, list)
    assert isinstance(resp[0], Films)

#Test in select drama films
def test_select_drama_films(): #TEST CLASS, NEED BE PREFIX "test_"
    film_rep = Filmsrepository(ConnectionHandlerMock)
    resp = film_rep.select_drama_films()
    print()
    print(resp)
    assert isinstance(resp, Films)
    assert resp.title == "Yuri"
    #assert resp.title == "João" #-> FORCE ERROR

def test_insert(): #TEST CLASS, NEED BE PREFIX "test_"
    film_rep = Filmsrepository(ConnectionHandlerMock)
    resp = film_rep.insert("something","AAAA", 22)
    print()
    print(resp)
