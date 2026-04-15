import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parent.parent
if str(_REPO) not in sys.path:
    sys.path.insert(0, str(_REPO))

from langchain_openai import ChatOpenAI

from pe_shared.env import load_project_env, require_openai_key
from pe_shared.llm_output import print_llm_result

load_project_env(__file__)
require_openai_key()

msg1 = "What is the capital of Brazil?"

msg2 = """
Find the user intent in the following text:
I'm looking for a restaurant in the center of Rio de Janeiro who has ratings above 4.5 for Japanese food.
"""

msg3 = "What's Brazil's capital? Respond only with the capital name and nothing else."

llm = ChatOpenAI(model="gpt-5-nano")

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result("msg1", response1)
print_llm_result("msg2", response2)
print_llm_result("msg3", response3)
