import psycopg2
import numpy as np
from ml_service.text_embedding import get_embeddings
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker

id = 0

def list_to_str(list_emb):
    text = '['
    for elem in list_emb:
        text+=str(elem)+','
    text = text.strip(',')
    return text+']'

# def list_to_str(list_emb):
#     text = '('
#     for elem in list_emb:
#         text+=f"('[{str(elem)}]'), "
#     return text+')'

def add_vectors_to_db(text_chank, embedding):

    global id

    id +=1

    try:
        # engine = create_engine('postgresql+psycopg2://myuser:mypassword@localhost:5432/mydb')
        # # Session factory, bound to the engine
        # Session = sessionmaker(bind=engine)
        #
        # # Create a new session
        # session = Session()
        # with engine.connect() as connection:
        #     print(list_to_str(embedding))
        #     connection.execute(text(f"INSERT INTO embeddings (embedding) VALUES ('{list_to_str(embedding)}');"))

        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port=5432,
            database="mydb"
        )

        cur = conn.cursor()
        conn.autocommit = True

        to_db = f"INSERT INTO embeddings (content, embedding) VALUES ('{text_chank}', '{list_to_str(embedding)}');"

        cur.execute(to_db)

        # Adding text chunk and embedding to the database
        # cur.execute(
        #     "INSERT INTO embeddings (content, embedding) VALUES (%s, %s)",
        #     (text_chank, list_to_str(embedding))
        # )

    except Exception as e:
        print("Error executing query", str(e))

    # finally:
    #     # Close communication with the PostgreSQL database server
    #     cur.close()
    #     conn.close()


def send_query_to_db(text_guery):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port=5432,
            database="mydb"
        )
        conn.autocommit = True

        cur = conn.cursor()

        # embedding guery
        query_embedding = get_embeddings(text_guery)

        # Perform a cosine similarity search
        cur.execute(
            """SELECT content FROM embeddings ORDER BY embedding <=> %s::vector LIMIT 5""",
            (query_embedding,)
        )

        # Fetch the result
        # context = []
        # for row in cur.fetchall():
        #     context.append(row[1])

        print(str(cur.fetchall()))
        return str(cur.fetchall())


    except Exception as e:
        print("Error executing query", str(e))

    finally:
        # Close communication with the PostgreSQL database server
        cur.close()
        conn.close()
