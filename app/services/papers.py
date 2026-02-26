from pathlib import Path


class PapersService:
    """
    只从本地 papers 目录读取数据。
    目前实现：列出若干文件，读取每个文件的一小段作为“上下文摘要”。
    """

    def __init__(self, base_dir: str | None = None) -> None:
        root = Path(base_dir) if base_dir else Path(".")
        self._papers_dir = root / "papers"

    def get_brief_context(self, max_files: int = 3, max_chars_per_file: int = 500) -> str:
        if not self._papers_dir.exists() or not self._papers_dir.is_dir():
            return "本地 papers 目录不存在或为空。"

        parts: list[str] = []
        count = 0

        for path in sorted(self._papers_dir.iterdir()):
            if count >= max_files:
                break
            if not path.is_file():
                continue

            try:
                text = path.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                continue

            snippet = text[:max_chars_per_file]
            parts.append(f"=== 文件: {path.name} ===\n{snippet}\n")
            count += 1

        if not parts:
            return "papers 目录中没有可读取的文件。"

        return "\n".join(parts)


