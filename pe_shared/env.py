import os
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parent.parent


def load_project_env(caller_file: str | Path | None = None) -> None:
    try:
        from dotenv import load_dotenv
    except ImportError:
        return

    root = repo_root()
    for rel in (
        ".env",
        "role-prompt/.env",
        "zero-shot/.env",
        "one-few-shot/.env",
    ):
        load_dotenv(root / rel)
    if caller_file is not None:
        load_dotenv(Path(caller_file).resolve().parent / ".env")


def require_openai_key() -> None:
    if not os.getenv("OPENAI_API_KEY"):
        raise RuntimeError(
            "Defina OPENAI_API_KEY no ambiente ou num ficheiro .env "
            "(raiz do repo, role-prompt/, zero-shot/, one-few-shot/ ou pasta do script)."
        )
