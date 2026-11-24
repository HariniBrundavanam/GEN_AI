### Week 6 – Llama 3.2 Baseline Evaluation

In Week 6, I developed a baseline evaluation system to test the performance of the Llama 3.2 model using a Golden Question Set containing 30 questions.

**Implementation Process:**

- Installed Ollama and downloaded the Llama 3.2 model.
- Created a Golden Question Set with expected answers, keywords, and sources.
- Connected the Python program to Ollama.
- Generated answers for all 30 questions.
- Implemented keyword-based scoring to evaluate responses.
- Classified results as PASS or REVIEW.
- Exported evaluation results into a CSV file.

**Commands Executed:**

```bash
ollama --version

ollama pull llama3.2

pip install -r requirements.txt

python main.py
```

**Outcome:** Successfully evaluated Llama 3.2 using keyword-based scoring and generated `baseline_results.csv` as the first baseline evaluation report (Release v0.1).
