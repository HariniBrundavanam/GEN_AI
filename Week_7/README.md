### Week 7 – Next Token Probabilities using Hugging Face Transformers

In Week 7, I developed a next-token prediction system using the DistilGPT-2 language model and Hugging Face Transformers. The main objective was to inspect raw logits and identify the top 5 most probable next-token candidates for a given input prompt.

**Implementation Process:**

- Installed PyTorch and Hugging Face Transformers.
- Loaded the pretrained DistilGPT-2 language model.
- Accepted a text prompt from the user.
- Converted the input text into tokens using the tokenizer.
- Passed the tokenized input through the language model.
- Extracted and displayed raw logits for the next-token prediction.
- Applied Softmax to convert logits into probability scores.
- Identified and displayed the top 5 next-token candidates using Top-K selection.
- Generated the most likely next token based on the highest probability.

**Commands Executed:**

```bash
pip install torch transformers
python main.py
```

**Outcome:** Successfully implemented a next-token probability inspection system using DistilGPT-2. Displayed raw logits, Softmax probabilities, and the top 5 predicted tokens for different input prompts, demonstrating how language models predict their next tokens.
