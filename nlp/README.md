# NLP API (FastAPI + Transformers)

A simple Natural Language Processing (NLP) API built with **FastAPI** and **Hugging Face Transformers**.
This project provides endpoints for sentiment analysis, named entity recognition (NER), text classification, and a combined analysis.

##  Features

*  Sentiment Analysis
*  Named Entity Recognition (NER)
* Text Classification
*  Combined NLP endpoint
*  Token-based authentication


## Installation

### 1. Clone the repository

git clone https://github.com/aysha312/nlp.git
cd nlp

### 2. Install dependencies

pip install -r requirements.txt

### 3. Run the server

uvicorn app.main:app --reload

##  API Documentation

Once the server is running, open:

* Swagger UI:
  http://127.0.0.1:8000/docs


## Authentication

All endpoints require a Bearer Token:

Authorization: student-access-2026


## Example Requests

### Sentiment Analysis

```json
POST /sentiment
{
  "text": "I love this product!"
}
```

### Named Entity Recognition (NER)

```json
POST /ner
{
  "text": "Elon Musk founded SpaceX in the United States."
}
```

### Text Classification

```json
POST /classification
{
  "text": "This is a great movie!"
}
```

## Combined Endpoint

```json
POST /combined
{
  "text": "Apple is opening a new office in Japan."
}
```


##  Technologies Used

* FastAPI
* Uvicorn
* Hugging Face Transformers
* PyTorch


##  Future Improvements

* Add database support
* Deploy to cloud (Render, Railway, AWS)
* Add more NLP models
* Improve authentication system





