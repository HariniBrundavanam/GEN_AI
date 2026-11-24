### Week 5 – Token Economics: Cost and Rate-Limit Budgeting

In Week 5, I developed a Token Economics budget planner to estimate the token usage and API cost of an LLM-powered feature before building it. I learned how to calculate daily and monthly expenses and check whether the expected requests fit within the configured API rate limits and budget.

**How I did it:**

Created a Python project with budget calculation and testing files.

Stored the feature assumptions, token prices, API limits and budget values in a .env file.

Used a Python dataclass to organize the budgeting details.

Calculated input tokens, output tokens and total daily token usage.

Estimated the daily and monthly API costs based on input and output token prices.

Checked RPM (Requests Per Minute) and TPM (Tokens Per Minute) limits.

Applied a safety margin to account for unexpected usage and traffic increases.

Added daily and monthly budget checks to generate a final recommendation.

Created test cases to verify cost calculations and rate-limit checks.

Performed what-if analysis by changing requests, token usage and other assumptions.

**Commands used:**

cd TokenEconomics

python -m venv .venv

.venv\Scripts\activate

pip install -r requirements.txt

python budget.py

python -m unittest test_budget.py

**Result:** Successfully developed a Python-based token budgeting tool that estimates LLM usage costs, checks rate limits and generates a recommendation to determine whether a proposed AI feature is within the configured budget and capacity limits.
