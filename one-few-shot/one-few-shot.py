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
Example:
Question: What is the capital of Brazil?
Answer: Brasília

Question: What is the capital of France?
Answer: 
"""

msg2 = """
Example:
Input: Database connection lost on server 10:45 AM.
Output: ERROR

Now Classify the following input:
Input: Disk usage at 80%.
Output: 
"""

msg3 = """
Classify the log severity of the following input:

Example 1:
Input: Database connection lost on server 10:45 AM.
Output: ERROR

Example 2:
Input: Disk usage at 80%.
Output: WARNING

Example 3:
Input: Database response time is above the threshold at 30ms.
Output: WARNING

Example 4:
Input: User logged in successfully.
Output: INFO

Now Classify the following input:
Input: API response is above the threshold.
Output: 
"""

msg4 = """
Classify the log severity of the following input:

Example 1:
Input: Database connection lost on server 10:45 AM.
Output: ERROR

Example 2:
Input: Disk usage at 80%.
Output: WARNING

Example 3:
Input: User logged in successfully.
Output: INFO

Example 4:
Input: File not found: config.json
Output: ERROR

Example 5:
Input: High memory usage detected: 75% of total memory.
Output: WARNING

Example 6:
Input: Background job finished successfully.
Output: INFO

Example 7:
Input: Retrying request to payment gateway.
Output: ERROR

Example 8:
Input: Disk usage at 90%.
Output: ERROR

Example 9:
Input: API latency is above the threshold.
Output: WARNING

Example 10:
Input: Scheduled backup completed successfully.
Output: INFO

Example 11:
Input: Low disk space detected: 15% left
Output: WARNING

Example 12:
Input: Low disk space detected: 5% left
Output: ERROR

Example 13:
Input: Cache warming completed
Output: INFO

Example 14:
Input: Connection timeout, retrying...
Output: WARNING

Example 15:
Input: Authentication failed for user admin
Output: ERROR

Now Classify the following input:
Input: GPU usage is 95%
Output: 
"""

llm = ChatOpenAI(model="gpt-5-nano")

response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)
response3 = llm.invoke(msg3)
response4 = llm.invoke(msg4)

print_llm_result("msg1", response1)
print_llm_result("msg2", response2)
print_llm_result("msg3", response3)
print_llm_result("msg4", response4)