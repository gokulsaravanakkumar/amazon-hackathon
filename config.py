import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
    USE_BEDROCK = os.getenv("USE_BEDROCK", "false").lower() == "true"

settings = Settings()