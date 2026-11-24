### Week 4 – Comparison of BPE, WordPiece and SentencePiece Tokenizers

In Week 4, I explored different tokenization techniques used in Large Language Models. I implemented and compared BPE, WordPiece and SentencePiece tokenizers to understand how they split text into smaller tokens. I tested them using English, Telugu and Hindi sentences and observed the differences in token counts.

**How I did it:**

Created a Python file to compare different tokenizers.

Installed the required libraries using the Transformers library and SentencePiece.

Used GPT-2 for BPE tokenization.

Used Multilingual BERT for WordPiece tokenization.

Used XLM-R for SentencePiece tokenization.

Provided sample sentences in English, Telugu and Hindi.

Displayed the generated tokens, token IDs and total token count for each tokenizer.

Compared the results to understand how different tokenizers process different languages.

**Commands used:**

cd Week4

pip install -r requirements.txt

python tokenizer_comparison.py

**Result:** Successfully implemented and compared three tokenization approaches using English, Telugu and Hindi text and understood how different tokenizers split sentences into tokens and generate token IDs.
