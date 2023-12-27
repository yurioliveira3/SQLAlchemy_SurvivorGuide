from sqlalchemy import create_engine

#Object PG + Driver Psycopg2
eng = create_engine(
    "postgresql+psycopg2://postgres:postgres@localhost:5432/cinema",
    execution_options={"isolation_level": "REPEATABLE READ"},
)

#Create connection
conn = eng.connect()

#Execute a select in DB
response = conn.execute('SELECT * FROM filmes')

#Print response
for row in response:
    print(row) #Print absolute row
    print(row.titulo) #Print only the title column