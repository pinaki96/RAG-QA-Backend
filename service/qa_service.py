import openai
import numpy as np
from model.document_model import Document
from utils.embedding_utils import generate_embedding
from conf_environment.conf_env import Config


class QAService:
    @staticmethod
    def process_question(question, document_ids=[]):
        """Processes a question by retrieving relevant documents and generating an answer."""
        try:
            # Generate embedding for the question
            question_embedding = generate_embedding(question)

            # Retrieve relevant documents based on embeddings
            relevant_docs = Document.retrieve_relevant_documents(question_embedding, document_ids)

            if not relevant_docs:
                return {"answer": "No relevant documents found."}

            # Combine retrieved content as context
            combined_content = " ".join([doc.content for doc in relevant_docs])

            # Generate answer using OpenAI GPT
            answer = QAService.generate_answer(combined_content, question)

            return {"question": question, "answer": answer}
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def generate_answer(context, question):
        """Generates a natural language answer using OpenAI GPT."""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                api_key=Config.OPENAI_API_KEY,
                messages=[
                    {"role": "system", "content": "You are a helpful AI assistant."},
                    {"role": "user", "content": f"Context: {context} \nQuestion: {question}"}
                ]
            )
            return response["choices"][0]["message"]["content"]
        except Exception as e:
            print("Error generating answer:", e)
            return "Error generating answer."
