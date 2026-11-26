import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# Step 1: Load a small pretrained language model
model_name = "distilgpt2"

print("Loading model...")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

model.eval()

print("Model loaded successfully!\n")

# Step 2: Take input from the user
prompt = input("Enter your prompt: ")

# Step 3: Convert prompt into token IDs
inputs = tokenizer(prompt, return_tensors="pt")

print("\nInput Tokens:")
print(tokenizer.convert_ids_to_tokens(inputs["input_ids"][0]))

# Step 4: Pass input through the model
with torch.no_grad():
    outputs = model(**inputs)

# Step 5: Extract logits for the last position
logits = outputs.logits[0, -1, :]

print("\nRaw Logits (first 10):")
print(logits[:10])

# Step 6: Convert logits into probabilities using Softmax
probabilities = torch.softmax(logits, dim=-1)

# Step 7: Find the top 5 most probable next tokens
top_k = 5

top_probs, top_ids = torch.topk(probabilities, top_k)

print("\nTop 5 Next Token Predictions:")
print("--------------------------------")

for i in range(top_k):
    token = tokenizer.decode([top_ids[i].item()])
    probability = top_probs[i].item() * 100

    print(f"{i + 1}. Token: {repr(token)} | Probability: {probability:.4f}%")

# Step 8: Generate the next token
next_token_id = torch.argmax(probabilities).item()
next_token = tokenizer.decode([next_token_id])

print("\nMost Likely Next Token:")
print(repr(next_token))

print("\nExperiment completed successfully!")
