### Week 2 – Provider-Agnostic LLM Client

In Week 2, I created an LLM client that works with both Gemini and Ollama. I learned how to use two different AI models through a common interface and switch between them based on user choice.

**How I did it:**

Created separate classes for Gemini and Ollama.

Installed Ollama and downloaded the Llama 3.2 model.

Created a common interface to connect both AI providers.

Used an LLMClient class to handle requests from both providers.

Added an option to select Gemini or Ollama while running the program.

Stored the Gemini API key in a .env file.

Created a test file to check whether the LLM client was working correctly.

**Commands used:**

ollama --version

ollama pull llama3.2

cd week-2

pip install -r requirements.txt

python main.py

python -m unittest test_client.py

**Result:** Successfully connected both Gemini and Ollama using one common LLM client and tested the working of the application.
