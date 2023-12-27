from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = 'postgresql+psycopg2://postgres:postgres@localhost:5432/cinema'
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string, 
            execution_options={"isolation_level": "REPEATABLE READ"},
        )
        return engine

    def get_engine(self):
        return self.__engine

    #Always when enter in class, create session
    def __enter__(self): 
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self #Return the context

    #Always when exit in class, close session
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()