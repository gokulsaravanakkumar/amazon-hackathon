from fastapi import APIRouter
from app.models.schemas import DebugRequest
from app.services.llm_service import generate_response
from app.utils.prompt_templates import debug_prompt

router = APIRouter()

@router.post("/")
def debug_error(request: DebugRequest):

    prompt = debug_prompt(request.error)

    response = generate_response(prompt)

    return {"response": response}