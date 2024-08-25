# simple-rag-chat-bot

This is a simple chat bot that uses the RAG model to generate responses. The RAG model is a retrieval-augmented generation model that uses a retriever to find relevant passages and a generator to generate responses. This chat bot uses the RAG model to generate responses to user queries.

## Prerequisites
- Install poetry
- Install npx
- Install pnpm
- Install fnm

## Installation
```
make build
```

Prepare the environment:
Create a `.env` file in the backend and frontend directory and add the following environment sample file. After that, replace the values with your own values.

## Prepare data
```
make data
```

## Embedding
```
make generate
```

## Run backend
```
make backend
```

## Run frontend
```
make frontend
```

## Report
https://docs.google.com/document/d/1htiXmZwBRYdYTt1f3QnNXqIgWMlDzl7XG6jh8LSHj6g/edit?usp=sharing