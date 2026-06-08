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



how my backend will works:
1) User sends a question through an API endpoint.
2) Flask receives the request.
3) Using AWS SDK (Boto3), the application securely retrieves the SambaNova API key from AWS Secrets Manager.
4) The SambaNova SDK sends the user's question to the LLM.
5) A telecom-specific system prompt restricts the model to answer only telecom-related questions.
6) The response is returned to the user as JSON.
