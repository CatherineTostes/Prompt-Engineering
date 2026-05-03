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
You are a Go backend engineer helping debug a REST API.
Use the ReAct style reasoning: alternative between "Thought:" (Your reasoning) and "Action:" (a concrete step or 
check you would perform).
After each action, write "Observation:" to capture what you found.
At the end, conclude with "Final Answer:" as your recommended fix.

Do not fabricate any information that is not provided in the context. Example: if the context does not provide 
error logs, do not use error logs in your reasoning.

Context: A user reports that the endpoint `POST /products` always returns HTTP 500.

Here is the handler code for `POST /products`:

```go
func CreateProduct(w http.ResponseWriter, r *http.Request) {
    var product Product
    err := json.NewDecoder(r.Body).Decode(&product)
    if err != nil {
        http.Error(w, "Bad Request", http.StatusBadRequest)
        return
    }
    stmt, err := db.Prepare("INSERT INTO products (id, name, description, price, stock) VALUES (?, ?, ?, ?, ?)")
    if err != nil {
        log.Fatal("Error")
    }

    _, err = stm.Exec(product.ID, product.Name, product.Description, product.Price, product.Stock)
    if err != nil {
        log.Println("Error during Exec:", err)
        http.Error(w. "Internal Server Error", http.StatusInternalServerError)
        return
    }

    w.WriteHeader(http.StatusCreated)
}

type Product struct {
    ID string `json="id"`
    Name string `json="name"`
    Description string `json="description"`
    Price string `json="price"`
    Stock int `json="stock"`
}
```
"""

msg2 = f"""
You are a travel planner helping a family choose the best way to go from Orlando to New York next month.
Use the ReAct style reasoning: alternate between "Thought: " (your reasoning) and "Action: " (a step such as 
checking flight time, cost or convenience).
After each action, write "Observation: " with what you found.
At the end, conclude with "Final Answer:" as your recomendation.

Context:
- The family has two adults and 2 children (ages 5 and 8)
- Budget: max $1,000 for transport (not include hotel)
- Dates: They must arrive on July 10 on the evening
- Options:
    -**Flight**: $220 per person round trip, 3-hour flight, plus $80 total in baggage fees.
    -**train**: $150 per person round trip, 20-hour journey, with onboard wifi and beds available for $50 extra per 
    person.
    -**Car Rental**: $60/day, 2 days of driving each way (gas + tolls estimated $250 total). Kids get restless on 
    long trips.

Other details:
- The kid's school finishes on July 9 at noon.
- Parents prefer not to arrive too tired, since they have a family weeding on July 11 in the morning.

Start you reasoning now.
"""

llm = ChatOpenAI(model="gpt-5-nano")

# response1 = llm.invoke(msg1)
response2 = llm.invoke(msg2)

# print_llm_result("msg1", response1)
print_llm_result("msg2", response2)