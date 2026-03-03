from app.config import settings
import boto3
import json

def local_response(prompt: str):
    return f"AI Explanation:\n\n{prompt[:500]}..."

def bedrock_response(prompt: str):

    client = boto3.client(
        service_name="bedrock-runtime",
        region_name=settings.AWS_REGION
    )

    body = json.dumps({
        "prompt": prompt,
        "max_tokens_to_sample": 500,
        "temperature": 0.3
    })

    response = client.invoke_model(
        modelId="anthropic.claude-3-sonnet-20240229-v1:0",
        body=body
    )

    result = json.loads(response["body"].read())
    return result["completion"]

def generate_response(prompt: str):
    if settings.USE_BEDROCK:
        return bedrock_response(prompt)
    return local_response(prompt)