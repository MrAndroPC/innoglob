from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
import requests
from ml_api.db.database import get_db

router = APIRouter()

class RAGRequest(BaseModel):
    text: str

def mock_find_similar_embeddings(request_text):
    # Placeholder function to simulate database response
    return {"query_text": "Sample query text", "context": ["Context part 1", "Context part 2"]}

def send_to_llama(prompt_text: str):
    llama_url = "https://mts-aidocprocessing-case-backup.olymp.innopolis.university/generate"
    headers = {"Content-Type": "application/json"}
    payload = {
        "prompt": prompt_text,
        "apply_chat_template": True,
        "system_prompt": "You are a helpful assistant.",
        "best_of": 0,
        "frequency_penalty": 0,
        "max_tokens": 1600,
        "n": 1,
        "presence_penalty": 0,
        "stream": False,
        "temperature": 1,
        "top_p": 1,
        "request_priority": 1,
        "top_k": -1,
        "min_p": 0,
        "repetition_penalty": 1,
        "length_penalty": 1,
        "early_stopping": False,
        "stop_token_ids": [0],
        "ignore_eos": False,
        "min_tokens": 100,
        "skip_special_tokens": True,
        "spaces_between_special_tokens": True,
        "include_stop_str_in_output": False
    }
    
    response = requests.post(llama_url, json=payload, headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to generate response from LLaMA.")
    return response.json()

@router.post("/send_rag_request")
def send_rag_request(request: RAGRequest, db: Session = Depends(get_db)):
    # Send the request text to the mock database query function
    db_response = mock_find_similar_embeddings(request.text)
    if not db_response:
        raise HTTPException(status_code=404, detail="No similar items found in the database.")
    
    # Format the query text and join the context list into a single prompt
    prompt_text = f"{db_response['query_text']} {' '.join(db_response['context'])}"
    
    # Send the prompt to LLaMA and get the response
    llama_response = send_to_llama(prompt_text)
    
    return {"llama_response": llama_response}


# from fastapi import APIRouter, HTTPException, Depends
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from ml_api.api.api_v1.endpoints.text_embedding import chunk_text, get_embeddings
# from ml_api.db.database import get_db, find_similar_embeddings

# router = APIRouter()

# class RAGRequest(BaseModel):
#     text: str

# @router.post("/send_rag_request")
# def send_rag_request(request: RAGRequest, db: Session = Depends(get_db)):
#     # Chunk and embed the input text
#     chunks = chunk_text(request.text)
#     embeddings_list = []
    
#     for chunk in chunks:
#         embeddings = get_embeddings(chunk)
#         if embeddings:
#             embeddings_list.append(embeddings)
    
#     if not embeddings_list:
#         raise HTTPException(status_code=400, detail="Failed to generate embeddings.")
    
#     # Search for similar embeddings in the database
#     results = find_similar_embeddings(embeddings_list, db)
#     return {"similar_items": results}
