### Week 1 – First LLM API Call Using Gemini

In Week 1, I built my first Python application that connects to Google's Gemini AI using an API key. I learned how to send questions to an AI model through an API and receive AI-generated responses directly in my program.

**How I did it:**

Created a Python project using the existing virtual environment.

Installed the required libraries using the requirements.txt file.

Generated a Gemini API key and stored it securely in a .env file.

Used the python-dotenv library to load the API key into the program.

Initialized the Gemini client using the google-genai library.

Sent prompts to Gemini using the generate_content() method.

Displayed the AI-generated responses in the terminal.

Experimented with different prompts to observe how the AI responses changed.

**Commands used:**

cd week1-llm-call

pip install -r requirements.txt

python main.py

**Result:** Successfully connected a Python application to Google's Gemini AI, sent different prompts and received AI-generated responses using the Gemini API.
