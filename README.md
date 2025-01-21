# PDF Assistant

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
git clone https://github.com/yourusername/pdf-assistant.git
cd pdf-assistant


### 2. Install Dependencies
python -m venv venv
source venv/bin/activate # On Windows use venv\Scripts\activate
pip install -r requirements.txt


### 3. Environment Setup
Create a `.env` file in project root:



### 4. Database Configuration
- Create PostgreSQL database named `ai`
- Update `db_url` in `app.py` if needed

## 🖥 Usage
Run assistant
python app.py
Start new conversation
python app.py --new
