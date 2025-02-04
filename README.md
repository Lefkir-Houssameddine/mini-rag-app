# mini-rag
This is a minimal implementation of the RAG model for question answering

## Requirements

- Python 3.8 or later

### Install Python using MiniConda 

1) download and install MiniConda from [here](https://docs.anaconda.com/miniconda/install/)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag-app python=3.8
```
3) Activate the environment :
```bash
$ conda activate mini-rag-app
```
## instalation
### install requirements :
```bash
$ pip install -r requirements.txt 
```
### Setup the environment variables
```bash
$ cp .env.exemple .env
```
Set your environment variables in the '.env' file. Like 'OPENAI_API_KEY' value.

## Run the FastAPI server
```bash
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```
## POSTMAN Collection 
Download the POSTMAN collection from [/assets/mini-rag-app.postman_collection.json](/assets/mini-rag-app.postman_collection.json)