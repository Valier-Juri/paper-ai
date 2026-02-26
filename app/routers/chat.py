from fastapi import APIRouter
from pydantic import BaseModel

from app.services.agent import AgentService


router = APIRouter(tags=["chat"])


class ChatRequest(BaseModel):
    message: str
    session_id: str | None = None


class ChatResponse(BaseModel):
    session_id: str
    reply: str


agent_service = AgentService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    session_id = request.session_id or "default"
    reply = await agent_service.handle_message(
        session_id=session_id,
        user_message=request.message,
    )
    return ChatResponse(session_id=session_id, reply=reply)


