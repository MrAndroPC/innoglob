from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from ml_api.core.config import settings

DATABASE_URL = f"postgresql://myuser:mypassword@{settings.VECTOR_DATABASE_URL}/mydb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to find similar embeddings
def find_similar_embeddings(embeddings_list, db):
    # Placeholder for similarity search logic
    query_results = []
    for embedding in embeddings_list:
        sql = text("SELECT id, content FROM items ORDER BY embedding <-> :embedding LIMIT 5")
        results = db.execute(sql, {"embedding": embedding}).fetchall()
        query_results.extend(results)
    return [{"id": row.id, "content": row.content} for row in query_results]
