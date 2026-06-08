# Telecom AI Assistant

## Domain
Telecommunications

## Model
DeepSeek-V3.1 (SambaNova)

## AWS Services Used
- EC2
- AWS SDK (Boto3)
- AWS Secrets Manager

## Features
- Telecom Question Answering
- Secure API Key Storage
- REST API Endpoint

## API

POST /ask

Request:

{
  "question": "What is 5G?"
}

Response:

{
  "question": "What is 5G?",
  "answer": "5G is the fifth generation..."
}
