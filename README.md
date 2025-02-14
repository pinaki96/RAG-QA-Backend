# RAG-QA-Backend

## 📌 Overview
This Flask-based API provides **document ingestion and Retrieval-Augmented Generation (RAG)** for answering user queries based on uploaded documents. The system extracts text from various file types, generates embeddings, stores them in PostgreSQL, and retrieves relevant documents for Q&A.

## 🚀 Features
- ✅ **File Upload Support**: Accepts PDFs, DOCX, TXT, XLSX, CSV, PPTX
- ✅ **Document Storage**: Saves extracted text in PostgreSQL
- ✅ **Embedding Generation**: Uses Hugging Face transformers for efficient retrieval
- ✅ **RAG-Based Q&A**: Retrieves relevant documents and generates answers using OpenAI GPT-4

---

## 📌 Installation
### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/pinaki96/RAG-QA-Backend.git
cd RAG-QA-Backend
```

### **2️⃣ Create a Virtual Environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate    # Windows
```

### **3️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4️⃣ Set Up Environment Variables**
Create a `.env` file and add:
```ini
DATABASE_URL=postgresql://username:password@localhost:5432/rag_db
OPENAI_API_KEY=your_openai_api_key
HUGGINGFACE_MODEL=sentence-transformers/all-MiniLM-L6-v2
```

### **5️⃣ Run the Application**
```bash
python app.py
```

---

## 📌 API Endpoints

### **1️⃣ Upload Document**
`POST /api/v1/document/upload`
#### **Request**
- `file`: Upload a document (`pdf`, `docx`, `xlsx`, `csv`, etc.)

#### **Response**
```json
{
  "message": "Document uploaded and processed successfully",
  "document": {
    "id": 1,
    "name": "test.pdf",
    "created_at": "..."
  }
}
```

### **2️⃣ List All Documents**
`GET /api/v1/document/list`
#### **Response**
```json
{
  "documents": [
    { "id": 1, "name": "test.pdf", "created_at": "..." }
  ]
}
```

### **3️⃣ Get Document by ID**
`GET /api/v1/document/get/{id}`
#### **Response**
```json
{
  "document": {
    "id": 1,
    "name": "test.pdf",
    "content": "Extracted text from the uploaded file..."
  }
}
```

### **4️⃣ Ask a Question**
`POST /api/v1/qa/ask`
#### **Request**
```json
{
  "question": "What is the document about?",
  "document_ids": [1]
}
```
#### **Response**
```json
{
  "question": "What is the document about?",
  "answer": "Based on retrieved documents: Extracted text from the uploaded file..."
}
```

### **5️⃣ Update Document**
`PUT /api/v1/document/update/{id}`
#### **Request**
```json
{
  "name": "Updated Test Document",
  "content": "This is the new content of the document."
}
```
#### **Response**
```json
{ "message": "Document updated successfully" }
```

### **6️⃣ Delete Document**
`DELETE /api/v1/document/delete/{id}`
#### **Response**
```json
{ "message": "Document deleted successfully" }
```

---

## 📌 Contributing
Feel free to fork this repository and submit a pull request if you want to contribute.

---

## 📌 License
This project is open-source and available under the MIT License.
