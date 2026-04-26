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
You are a senior software engineer.
A user report than an API request to the endpoint `/user` is taking 5 seconds to respond, wich is too slow.
Think in a Tree of Thought manner:
- Generate at least 3 different possible causes for this latency.
- For each cause, reason step by step about how likely it is and how you would verify it.
- Then compare the branches and choose the most plausible one as the primary hypothesis.
- Finish with a recommended next action to debug or fix the issue.
"""

msg2 = f"""
You are designing a service that processes millions of images daily.
Think in a Tree of Thought manner:
- Generate at least 3 different architecture options.
- For each option, reason step by step about scalability, cost, and complexity.
- Compare the options.
- Choose the best trade-off and explain why it is superior to the others.
- Finish with "Final Answer: " + the chosen option.
"""

msg3 = f"""
You are designing a service that processes millions of images daily.
Think in a Tree of Thought manner:
- Think about at least 3 different architecture options.
- For each option, reason step by step about scalability, cost, and complexity.
- Compare the options.
- Choose the best trade-off and explain why it is superior to the others.
- Finish with "Final Answer: " + the chosen option with 6 words or less.

- OUTPUT ONLY THE FINAL ANSWER, WITHOUT ANY OTHER TEXT.
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo")
llm = ChatOpenAI(model="gpt-5-nano") #reasoning model

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)

print_llm_result("msg1", response1)
print_llm_result("msg2", response2)
print_llm_result("msg3", response3)