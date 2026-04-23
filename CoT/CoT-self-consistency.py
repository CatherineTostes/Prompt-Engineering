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
Question: In an API endpoint that returns a list of users and theirs posts, the developer wrote:

users := db.FindAllUsers()
for _, u := range users {
    u.Posts = db.FindPostsByUserID(u.ID)
}

How many database queries will this code execute if there are N users?

Generate 3 different reasoning paths step by step
At the end, sumarize the answers and choose the most consistent one, ignoring outliers.
If there are 3 different answers, ONLY reply: "I can't find a consistent answer."
"""

# llm = ChatOpenAI(model="gpt-3.5-turbo") teste
llm = ChatOpenAI(model="gpt-5-nano") #reasoning model

response1 = llm.invoke(msg1)

print_llm_result("msg1", response1)