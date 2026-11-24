### Week 2 – Provider-Agnostic LLM Client

In Week 2, I developed an LLM client that supports both Google's Gemini and Ollama's Llama 3.2. The aim was to use different AI providers through a single common interface.

**Implementation Process:**

- Installed Ollama and downloaded the Llama 3.2 model.
- Created a common interface using an abstract class.
- Implemented separate classes for Gemini and Ollama.
- Developed an LLMClient to handle requests from both providers.
- Added an option to select the AI provider at runtime.
- Stored the Gemini API key in the `.env` file.
- Tested the client using a fake provider.

**Commands Executed:**

ollama --version

ollama pull llama3.2

cd week-2

pip install -r requirements.txt

python main.py

**Testing Command:**

python -m unittest test_client.py

**Outcome:** Successfully connected Gemini and Ollama through a single LLM client and tested its functionality.
