import os
from pathlib import Path

try:
    from dotenv import load_dotenv

    load_dotenv(Path(__file__).resolve().parent / ".env")
except ImportError:
    pass

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from utils import print_llm_result

try:
    import openai
except Exception:
    openai = None

if not os.getenv("OPENAI_API_KEY"):
    raise RuntimeError(
        "Defina OPENAI_API_KEY no ambiente ou num ficheiro .env na pasta do projeto."
    )

system_professor = """You are a university professor of computer science who is very technical
and explain concepts with forma definitions and pseudocode."""

system_student = """You are a high school student that is starting learning coding.
You are not very technical and you prefere to explain concepts with simple words and examples."""

user_message = "Explain recursion in 50 words or less."

chat_prompt_professor = ChatPromptTemplate.from_messages(
    [("system", system_professor), ("user", user_message)]
)
chat_prompt_student = ChatPromptTemplate.from_messages(
    [("system", system_student), ("user", user_message)]
)

llm = ChatOpenAI(model="gpt-5-nano")

chain_professor = chat_prompt_professor | llm
chain_student = chat_prompt_student | llm

try:
    response_professor = chain_professor.invoke({})
    response_student = chain_student.invoke({})
except Exception as e:
    if openai is not None and isinstance(e, getattr(openai, "RateLimitError", ())):
        raise SystemExit(
            "Erro 429 (quota insuficiente). A tua API key parece válida, mas a conta/projeto "
            "não tem créditos/quota disponível. Verifica Billing/Usage no painel da OpenAI."
        ) from e
    if openai is not None and isinstance(e, getattr(openai, "AuthenticationError", ())):
        raise SystemExit(
            "Erro de autenticação. Verifica se `OPENAI_API_KEY` está correta e ativa."
        ) from e
    raise SystemExit(f"Falha ao chamar a API: {e.__class__.__name__}: {e}") from e

print_llm_result("professor", response_professor)
print_llm_result("student", response_student)
