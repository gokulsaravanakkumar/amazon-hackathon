import os
from app.services.rag_service import add_document

def index_codebase(folder_path: str):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.endswith(".py"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8") as f:
                    content = f.read()
                    add_document(path, content)