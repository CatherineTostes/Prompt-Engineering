import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from pe_shared.env import load_project_env, require_openai_key
from pe_shared.llm_output import print_llm_result

load_project_env(__file__)
require_openai_key()

try:
    import openai
except Exception:
    openai = None

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
