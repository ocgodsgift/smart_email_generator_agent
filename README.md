⚙️ Installation

Clone the repo:
git clone https://github.com/yourusername/smart_email_generator_agent.git
cd smart_email_generator_agent

Create & activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Add your OpenAI API key to .env:
OPENAI_API_KEY=your_api_key_here

▶️ Usage
Run the crew directly
python run.py --topic "Follow-up email after interview"

Run API server
uvicorn api.main:app --reload

Test with:
curl -X POST "http://127.0.0.1:8000/generate_email" \
     -H "Content-Type: application/json" \
     -d '{"topic": "Schedule a meeting with client"}'

🧩 Example Output

Input:
Topic: "Project deadline extension request"

Output:
Subject: Request for Project Deadline Extension  
Dear [Recipient’s Name],  
I hope this message finds you well. I am writing to request an extension on the upcoming project deadline due to unforeseen challenges...  
