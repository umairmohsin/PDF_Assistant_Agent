# PDF Assistant Agent 

## Overview
A sophisticated AI-powered PDF assistant that leverages OpenAI embeddings and PostgreSQL for intelligent document interaction.

## 🚀 Features
- Load PDF documents from URLs
- AI-powered document querying
- Interactive CLI interface
- Persistent conversation storage
- Vector-based knowledge retrieval

## 🛠 Prerequisites
- Python 3.7+
- PostgreSQL
- OpenAI API Key

## 📦 Installation

### 1. Clone Repository
- git clone https://github.com/umairmohsin/PDF_Assistant_Agent.git
- cd PDF_Assistant_Agent

### 2. Install Dependencies
- python -m venv venv
- source venv/bin/activate # On Windows use venv\Scripts\activate
- pip install -r requirements.txt

### 3. Environment Setup
Create a `.env` file in project root:

### 4. Database Configuration
- You can run this Docker command to setup the postgres database:
docker run -d \
  -e POSTGRES_DB=ai \
  -e POSTGRES_USER=ai \
  -e POSTGRES_PASSWORD=ai \
  -e PGDATA=/var/lib/postgresql/data/pgdata \
  -v pgvolume:/var/lib/postgresql/data \
  -p 5532:5432 \
  --name pgvector \
  phidata/pgvector:16


## 🖥 Usage
- Install Requirements (pip install -r requirements.txt) 
- Run assistant
- python app.py
