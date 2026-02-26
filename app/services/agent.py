from app.services.gemini_client import GeminiClient
from app.services.papers import PapersService


class AgentService:
    """
    Minimal agent service:
    - 接收用户消息
    - 从本地 papers 目录取资料（目前只是简单拼接）
    - 调用 Gemini 生成回复（当前可先用占位实现）
    """

    def __init__(self) -> None:
        self._gemini = GeminiClient()
        self._papers = PapersService()

    async def handle_message(self, session_id: str, user_message: str) -> str:
        # 1. 从本地 papers 目录获取一些上下文（目前取前几个文件的开头内容作为示例）
        context = self._papers.get_brief_context()

        # 2. 调用 Gemini（当前实现为占位，如果没配置 API Key，就本地回声）
        reply = await self._gemini.chat(
            user_message=user_message,
            context=context,
        )
        return reply


