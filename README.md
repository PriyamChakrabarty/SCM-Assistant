# SCM Assistant

Supply Chain Management Assistant built using Flowise.

## Objective

Build a RAG chatbot capable of answering questions about:

- Supplier Performance Data
- Governance Policy

## Tech Stack

- Flowise Cloud
- Google Gemini 2.5 Flash
- Chroma Vector Database
- FastAPI Analytics Layer
- Python

---

## Architecture

User
↓
Flowise Agent
↓
Retriever + Analytics Tools
↓
Gemini
↓
Response

---

## Chunk Experiment 1

Chunk Size: 500

Chunk Overlap: 50

Result:

- Faster retrieval
- Less context

---

## Chunk Experiment 2

Chunk Size: 1200

Chunk Overlap: 200

Result:

- Better policy retrieval
- Better certification retrieval

Chosen Configuration:

Chunk Size: 1200

Chunk Overlap: 200

---

## Public Chatbot URL

https://cloud.flowiseai.com/chatbot/XXXXX

---

## LLM

Gemini 2.5 Flash

---

## Embeddings

Google Embeddings

---

## Sample Question Results

(Add screenshots and answers here)

---

## Future Improvements

- SQL Agent
- Real-time supplier updates
- Dashboard
- Multi-agent architecture