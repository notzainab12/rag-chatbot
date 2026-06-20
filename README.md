# *RAG Document Search*

*A Retrieval-Augmented Generation (RAG) application that enables users to query documents using Large Language Models (LLMs). The system retrieves relevant document chunks using vector similarity search and generates context-aware responses.*
<img width="1046" height="621" alt="image" src="https://github.com/user-attachments/assets/9f35dcdc-81ae-4bcc-8f98-435aee33e3c2" />
<img width="856" height="540" alt="image" src="https://github.com/user-attachments/assets/accf8924-7678-41b0-ad8b-0326289a3ddb" />
<img width="908" height="630" alt="image" src="https://github.com/user-attachments/assets/8aff1cb7-b789-43d6-bac7-3d1ea8ea4a89" />
<img width="808" height="579" alt="image" src="https://github.com/user-attachments/assets/1839aff6-f29b-4a44-8f31-c0f614d2e47a" />

---

## *Features*

*• PDF document ingestion and processing*
*• Text chunking and preprocessing*
*• HuggingFace Embeddings for semantic search*
*• FAISS vector database for efficient retrieval*
*• LangGraph workflow orchestration*
*• Groq LLM integration for answer generation*
*• Interactive Streamlit user interface*

---

## *Tech Stack*

*Python*
*Streamlit*
*LangChain*
*LangGraph*
*FAISS*
*HuggingFace Embeddings*
*Groq API*

---

## *Project Structure*

```text
src/
├── config/
├── document_ingestion/
├── graph_builder/
├── nodes/
├── state/
└── vectorstore/

streamlit_app.py
main.py
requirements.txt
pyproject.toml
uv.lock
```

---

## *Installation*

*Clone the repository:*

```bash
git clone https://github.com/notzainab12/rag-chatbot.git
cd rag-chatbot
```

*Create a virtual environment:*

```bash
python -m venv .venv
```

*Activate the environment:*

```bash
.venv\Scripts\activate
```

*Install dependencies:*

```bash
pip install -r requirements.txt
```

*Create a `.env` file and add your API key:*

```env
GROQ_API_KEY=your_api_key
```

---

## *Run the Application*

```bash
streamlit run streamlit_app.py
```

*The application will be available at:*

```text
http://localhost:8501
```

---

## *Workflow*

*1. Load and process documents*
*2. Split text into chunks*
*3. Generate embeddings*
*4. Store vectors in FAISS*
*5. Retrieve relevant chunks based on user query*
*6. Generate answers using Groq LLM*

---
---

## *Author*

***Zainab***
*B.Tech *
*Indira Gandhi Delhi Technical University for Women*
