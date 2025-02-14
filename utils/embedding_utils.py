import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
from conf_environment.conf_env import Config

# Load pre-trained embedding model (Hugging Face)
tokenizer = AutoTokenizer.from_pretrained(Config.HUGGINGFACE_MODEL)
model = AutoModel.from_pretrained(Config.HUGGINGFACE_MODEL)

def generate_embedding(text):
    """Generates an embedding for the given text using a transformer model."""
    try:
        inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = model(**inputs)
        embedding = outputs.last_hidden_state[:, 0, :].numpy()
        return embedding.tobytes()  # Store as binary for database storage
    except Exception as e:
        print("Error generating embedding:", e)
        return None
