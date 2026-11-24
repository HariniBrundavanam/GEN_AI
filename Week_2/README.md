### Week 2 – Provider-Agnostic LLM Client

In Week 2, I developed a flexible LLM client that supports both Google's Gemini (cloud-based) and Ollama's Llama 3.2 (locally running model). The main goal was to interact with different AI providers using a single common interface without changing the main application logic.

**Implementation Process:**
- Installed Ollama and downloaded the Llama 3.2 model for local execution.
- Created a common `LLMProvider` interface using an abstract class.
- Implemented separate provider classes for Gemini and Ollama.
- Developed an `LLMClient` to communicate with either provider.
- Added provider selection so users can choose between Gemini and Ollama at runtime.
- Stored the Gemini API key securely in the `.env` file.
- Created a test file with a fake provider to verify the client's functionality.

**Commands Executed:**
ollama --version
ollama pull llama3.2

cd week-2
pip install -r requirements.txt
python main.py


**Testing Command:**
python -m unittest test_client.py

**Outcome:** Successfully implemented and tested a provider-independent LLM client that can generate AI responses using either a hosted Gemini API or a locally running Ollama model through the same interface.
