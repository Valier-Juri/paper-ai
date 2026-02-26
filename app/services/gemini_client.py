import os

import httpx


class GeminiClient:
    """
    极简 Gemini 客户端。
    - 如果设置了 GEMINI_API_KEY，则调用 Gemini（这里只写伪代码结构，便于你替换成正式 SDK/HTTP 调用）
    - 如果没设置，则直接返回一个本地拼接的占位回复，方便开发调试
    """

    def __init__(self) -> None:
        self._api_key = os.getenv("GEMINI_API_KEY")
        # 这里只是示意，实际 endpoint / 模型名称请按官方文档替换
        self._endpoint = os.getenv("GEMINI_API_ENDPOINT", "").rstrip("/")
        self._model = os.getenv("GEMINI_MODEL", "gemini-1.5-pro")

    async def chat(self, user_message: str, context: str | None = None) -> str:
        if not self._api_key or not self._endpoint:
            # 占位逻辑：不真正调用外部 API，方便你先把后端跑起来
            prefix = "[本地调试模式：未配置 GEMINI_API_KEY/GEMINI_API_ENDPOINT]\n"
            ctx = f"\n\n[来自 papers 的上下文摘要]\n{context}" if context else ""
            return prefix + f"你说的是：{user_message}" + ctx

        # 下面是一个极简的 HTTP 调用示意，你需要根据 Gemini 正式接口格式自行调整
        payload = {
            "model": self._model,
            "messages": [
                {
                    "role": "system",
                    "content": "你是一个帮助用户写论文的助手，只能根据提供的本地 papers 内容回答。",
                },
                {
                    "role": "user",
                    "content": user_message,
                },
            ],
        }

        if context:
            payload["messages"].insert(
                1,
                {
                    "role": "system",
                    "content": f"以下是本地 papers 目录中的部分内容，你的回答只能基于这些内容：\n{context}",
                },
            )

        headers = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

        async with httpx.AsyncClient(timeout=30.0) as client:
            resp = await client.post(self._endpoint, json=payload, headers=headers)
            resp.raise_for_status()
            data = resp.json()

        # 根据实际返回结构取出文本，这里写成占位：
        text = data.get("choices", [{}])[0].get("message", {}).get("content") or ""
        return text or "Gemini 返回了空结果，请检查配置和请求格式。"


