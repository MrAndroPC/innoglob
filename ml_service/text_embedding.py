import requests


# Define a function to get embeddings from the embedder API
def get_embeddings(text):
    url = "https://mts-aidocprocessing-case-embedder.olymp.innopolis.university/embed"
    payload = {
        "inputs": text,
        "normalize": True,
        "truncate": False,
        "truncation_direction": "Right"
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        # Extracting the first embedding list from the response
        return response.json()[0]  # Assuming the response is structured as shown
    else:
        print(f"Error fetching embeddings: {response.status_code}, {response.text}")
        return None


# Chunking function
def chunk_text(text, chunk_size=100, chunk_overlap=30):
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunks.append(' '.join(words[start:end]))
        start += (chunk_size - chunk_overlap)
    return chunks
