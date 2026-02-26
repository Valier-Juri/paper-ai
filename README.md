# paper-ai

## 简单后端架构说明（FastAPI）

项目里已经内置了一个最简后端，用于对接 Gemini，并且**只从本地 `papers` 目录读取数据源**。

### 目录结构（后端相关）

```text
.
├── app
│   ├── main.py                # FastAPI 入口
│   ├── routers
│   │   └── chat.py            # /api/chat 对话接口
│   └── services
│       ├── agent.py           # AgentService，协调 Gemini + papers
│       ├── gemini_client.py   # 极简 Gemini 客户端（含本地调试模式）
│       └── papers.py          # 只读访问本地 papers 目录
├── papers/                    # 本地论文/素材目录（需手动创建）
├── requirements.txt
└── .env.example
```

### 本地运行步骤

1. 安装依赖：

```bash
pip install -r requirements.txt
```

2.（可选）复制环境变量模板并填写 Gemini 配置：

```bash
cp .env.example .env
# 编辑 .env 写入 GEMINI_API_KEY 和 GEMINI_API_ENDPOINT
```

3. 创建本地 `papers` 目录，并放入一些 `.txt` 或其他文本文件（UTF-8 编码为佳）：

```bash
mkdir -p papers
```

4. 启动服务：

```bash
uvicorn app.main:app --reload --port 8000
```

5. 测试接口：

```bash
curl -X POST "http://localhost:8000/api/chat" \
  -H "Content-Type: application/json" \
  -d '{"message": "帮我写一个关于AIGC教育应用的研究问题示例"}'
```

如果没有配置 Gemini 相关环境变量，接口会返回一个**本地调试模式**的占位回复，同时把从 `papers` 目录读取到的部分内容附在后面，便于确认“只从 papers 取数据源”的逻辑是否正常工作。
