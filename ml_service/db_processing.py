import psycopg2
import numpy as np
from text_embedding import get_embeddings


def list_to_str(list_emb):
    text = '['
    for elem in list_emb:
        text+=str(elem)+', '
    text = text.strip(', ')
    return text+']'

def add_vectors_to_db(text_chank, embedding):
    try:
        # Establish a connection to the PostgreSQL database
        conn = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port=5432,
            database="mydb"
        )

        cur = conn.cursor()

        # Adding text chunk and embedding to the database
        cur.execute(
            "INSERT INTO embeddings (content, embedding) VALUES (%s, %s::vector)",
            (text_chank, list_to_str(embedding))
        )

    except Exception as e:
        print("Error executing query", str(e))

    finally:
        # Close communication with the PostgreSQL database server
        cur.close()
        conn.close()


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

        cur = conn.cursor()

        # embedding guery
        query_embedding = get_embeddings(text_guery)

        # Perform a cosine similarity search
        cur.execute(
            """SELECT id, content, 1 - (embedding <=> %s) AS cosine_similarity
               FROM items
               ORDER BY cosine_similarity DESC LIMIT 5""",
            (query_embedding,)
        )

        # Fetch the result
        context = []
        for row in cur.fetchall():
            context.append(row[1])

        result_dict = {'text guery': text_guery, 'context': context}

        return result_dict

    except Exception as e:
        print("Error executing query", str(e))

    finally:
        # Close communication with the PostgreSQL database server
        cur.close()
        conn.close()