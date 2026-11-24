### Week 3 – LLM Monitoring with MongoDB

In Week 3, I extended my previous LLM client by adding a monitoring system using MongoDB. I worked on tracking token usage, response time and estimated API cost for every AI request. I also added error handling and retry options to make the application more reliable.

**How I did it:**

Created a MongoDB Atlas account and connected it to my Python project.

Stored the Gemini API key and MongoDB connection string in the .env file.

Created a usage_logger.py file to store LLM usage details in MongoDB.

Updated llm_client.py to track input tokens, output tokens, response time and estimated cost.

Added timeout and retry handling for temporary errors.

Updated main.py to connect the selected AI provider with the MongoDB logger.

Created a test file to check response generation and usage logging.

Verified the stored usage details in the MongoDB Atlas database.

**Commands used:**

cd Week3

pip install -r requirements.txt

python -m unittest test_client.py

python main.py

**Result:** Successfully integrated MongoDB with the LLM client to monitor AI requests, track token usage, measure response time, estimate cost and store request details in the database.
