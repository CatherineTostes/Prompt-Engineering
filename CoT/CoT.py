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

msg1 = """
Classify the log severity.

Input: Disk usage at 85%.
Answer: Only with INFO, WARNING or ERROR.
"""

msg2 = """
Classify the log severity.

Input: Disk usage at 85%.
Think step by step and answer only with INFO, WARNING or ERROR.
At the end, give only the final answer after "Answer:".
"""

msg3 = """
Question: How many "r" are in the word "strawberry"?
Answer only with the number of "r"s.
"""

msg4 = """
Question: How many "r" are in the word "strawberry"?
Explain step by step by breaking down each letter in bullets points, pointing out the "r" before giving the final answer.
Give the final result after "Answer:"
"""

llm = ChatOpenAI(model="gpt-5-nano") #reasoning model

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result("msg1", response1)
print_llm_result("msg2", response2)
print_llm_result("msg3", response3)
print_llm_result("msg4", response4)
