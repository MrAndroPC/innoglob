import os
import psycopg2

from ml_service.parser import take_all_files, get_links_to_files
from ml_service.pdf_processing import pdf_reader, write_to_txt
from ml_service.text_embedding import get_embeddings, chunk_text
from ml_service.db_processing import add_vectors_to_db, send_query_to_db

# # parsing files
# url = 'https://www.disclosure.ru/issuer/7740000076/'
# folder = "pdfci/"
#
# take_all_files(get_links_to_files(url), folder)
#
# # convert files from pdf to txt with taking text from images
# folder = "images/"
# folder1 = "processed_files/"
#
# for filename in os.listdir("pdfci"):
#     try:
#         text = pdf_reader("pdfci/" + filename, folder)
#         write_to_txt(text, folder1)
#     except Exception as e:
#         print(f"Error processing file {filename}")

# chanking and embedding files, load to db
# for file in os.listdir("processed_files"):
#     try:
#         with open('processed_files/4_file.txt', 'r', encoding='utf-8') as file:
#             embeddings = []
#             for elem in chunk_text(file.read()):
#                 embeddings.append([elem, get_embeddings(elem)])
#             for i in range(len(embeddings)):
#                 add_vectors_to_db(embeddings[i][0], embeddings[i][1])
#                 # send_to_database(embeddings[i][0], embeddings[i][1])
#     except Exception as e:
#         print()

conn = psycopg2.connect(
            user="myuser",
            password="mypassword",
            host="localhost",
            port=5432,
            database="mydb"
        )

table_create_command = """
        CREATE TABLE embeddings (id bigserial primary key, content TEXT, embedding vector(1024));
                    """

cur = conn.cursor()


# cur.execute("INSERT INTO cats (name, age) VALUES ('ssjjj', 13);")
# cur.execute("select * from cats;")
# print(cur.fetchall())
# cur.execute(table_create_command)

with open('processed_files/4_file.txt', 'r', encoding='utf-8') as file:
    embeddings = []
    for elem in chunk_text(file.read()):
        embeddings.append([elem, get_embeddings(elem)])
    for i in range(len(embeddings)):
        add_vectors_to_db(embeddings[i][0], embeddings[i][1])

