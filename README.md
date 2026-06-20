# SCM Assistant – Supply Chain RAG Chatbot

## Overview

SCM Assistant is an AI-powered Supply Chain Management chatbot built using Flowise, Google Gemini 2.5 Flash, Pinecone Vector Database, and FastAPI.

The project combines Retrieval-Augmented Generation (RAG) with supply chain analytics APIs to answer questions about supplier performance, governance policies, compliance requirements, disruptions, spend analysis, and supplier risk.

## Features

* RAG-based question answering using PDF and CSV data sources
* Semantic search with Pinecone Vector Database
* Google Gemini 2.5 Flash powered conversational AI
* FastAPI analytics services
* Supplier Watch List (SWL) analysis
* Volume rebate eligibility analysis
* Disruption and risk monitoring
* Regional spend analysis
* Product defect analytics
* Public Flowise chatbot deployment

## Tech Stack

### AI & RAG

* Flowise
* Google Gemini 2.5 Flash
* Pinecone Vector Database
* Mistral Embeddings

### Backend

* FastAPI
* Pandas
* Python

### Deployment

* Render
* Flowise Cloud

## Project Architecture

User Query
→ Flowise Agent
→ Pinecone Retrieval
→ Gemini 2.5 Flash
→ FastAPI Analytics Tools
→ Response

## API Endpoints

### Health Check

GET /

### Rebate Eligible Suppliers

GET /rebate

### Supplier Watch List

GET /swl

### Active Disruptions

GET /disruptions

### Regional Spend Analysis

GET /regional-spend

### Defect Analysis

GET /defects

## Deployment

### Flowise Chatbot

<ADD_FLOWISE_CHATBOT_URL>

### Backend API

https://scm-assistant.onrender.com/

## Repository Structure

```text
SCM-Assistant/
│
├── analytics/
├── backend/
├── data/
├── screenshots/
├── requirements.txt
├── README.md
└── scm_assistant.json
```

## Sample Questions

* Which suppliers qualify for the annual Volume Rebate Program?
* Which suppliers are on Supplier Watch List status?
* Which suppliers have active disruption flags?
* Which region has the highest procurement spend?
* Which product category has the highest average defect rate?

## Future Improvements

* Real-time supplier monitoring
* Dashboard integration
* Advanced risk prediction models
* Multi-agent workflow orchestration
* Automated supplier scorecards

## Author

Priyam Chakrabarty

GitHub:
https://github.com/PriyamChakrabarty

Project Repository:
https://github.com/PriyamChakrabarty/SCM-Assistant
