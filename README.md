# 📚 CiteWise AI - Research Agent with Citations

An intelligent AI-powered Research Agent that answers questions from user-uploaded documents using Retrieval-Augmented Generation (RAG). The system retrieves relevant information from uploaded documents, generates context-aware answers using a Large Language Model (LLM), and displays the supporting source citations.

---

## 🚀 Project Overview

CiteWise AI enables users to upload research documents (PDF, DOCX, or TXT), ask natural language questions, and receive accurate answers based only on the uploaded content.

Instead of relying solely on an LLM's internal knowledge, the application uses semantic search with vector embeddings to retrieve the most relevant document sections before generating the final response.

This approach minimizes hallucinations and improves answer reliability.

---

## ✨ Features

- Upload multiple PDF, DOCX, and TXT documents
- Automatic document parsing
- Intelligent text chunking
- Semantic search using Sentence Transformers
- Fast similarity search using FAISS
- AI-generated answers using Groq Llama
- Source citations for every response
- Clean and user-friendly Streamlit interface
- Handles missing information by informing the user when an answer is not available in the uploaded documents

---

## 🏗 System Architecture

```
User Uploads Documents
        │
        ▼
Document Parser
        │
        ▼
Text Chunking
        │
        ▼
Sentence Transformer Embeddings
        │
        ▼
FAISS Vector Database
        │
        ▼
Semantic Retrieval
        │
        ▼
Groq LLM
        │
        ▼
Answer Generation
        │
        ▼
Source Citations
```

---

## 🛠 Technology Stack

### Programming Language
- Python

### Frontend
- Streamlit

### AI / NLP
- Sentence Transformers (all-MiniLM-L6-v2)
- Groq Llama Model

### Vector Database
- FAISS

### Document Processing
- PyMuPDF
- python-docx

### Supporting Libraries
- NumPy
- python-dotenv

---

## 📂 Project Structure

```
CiteWiseAI/
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
│
├── core/
│   ├── parser.py
│   ├── chunker.py
│   ├── embedder.py
│   ├── vectorstore.py
│   ├── retriever.py
│   ├── llm.py
│   └── citations.py
│
└── sample_documents/
```

---

## ⚙ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/CiteWiseAI.git
```

Navigate into the project

```bash
cd CiteWiseAI
```

Create a virtual environment

```bash
py -m venv venv
```

Activate the virtual environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
GROQ_API_KEY=YOUR_API_KEY
```

Run the application

```bash
py -m streamlit run app.py
```

---

## 📖 How It Works

1. Upload one or more research documents.
2. Documents are parsed and converted into plain text.
3. Text is divided into smaller overlapping chunks.
4. Each chunk is converted into semantic embeddings.
5. Embeddings are stored in a FAISS vector database.
6. When a question is asked, the system retrieves the most relevant chunks.
7. Retrieved context is sent to the Groq LLM.
8. The generated answer is displayed along with the supporting source citations.

---

## 📸 Sample Workflow

Upload Document

↓

Ask Question

↓

Semantic Search

↓

Retrieve Relevant Chunks

↓

Generate Answer

↓

Display Citations

---

## 🎯 Design Decisions

- **FAISS** was chosen for fast and efficient vector similarity search.
- **Sentence Transformers** provide semantic embeddings instead of simple keyword matching.
- **Groq Llama** offers fast inference for real-time responses.
- **Streamlit** enables rapid development of an interactive user interface.
- **Document chunking** improves retrieval accuracy for long documents.

---

## ⚖ Trade-offs

### Advantages

- Fast document retrieval
- Semantic understanding of user queries
- Reduced hallucinations
- Easy to extend with additional document formats

### Limitations

- OCR is not supported for scanned PDFs.
- Retrieval quality depends on chunk size.
- Currently supports only uploaded local documents.
- No conversation memory between sessions.

---

## 🔮 Future Improvements

- OCR support for scanned documents
- Multi-document ranking
- Page-level citations
- Chat history
- Document summarization
- Web search integration
- Hybrid search (BM25 + Vector Search)
- Support for PowerPoint and Excel documents

---

## 👨‍💻 Author

**Hitharth K**

Bachelor of Engineering – Artificial Intelligence & Machine Learning

Project: CiteWise AI – Research Agent with Citations

---

## 📄 License

This project is developed for the ROOMAN AI Research Agent Assignment.
