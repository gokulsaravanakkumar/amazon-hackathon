from fastapi import APIRouter
from app.models.schemas import QueryRequest
from app.services.rag_service import retrieve_context
from app.services.llm_service import generate_response
from app.utils.prompt_templates import explain_prompt

router = APIRouter()

@router.post("/")
def explain_code(request: QueryRequest):

    context = retrieve_context(request.question)

    prompt = explain_prompt(context, request.question)

    response = generate_response(prompt)

    return {"response": response}