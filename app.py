from fastapi import FastAPI
from pydantic import BaseModel
from email_crew import email_crew

app = FastAPI(title="Email Generator API", version="1.0")

class EmailRequest(BaseModel):
    topic: str

@app.post("/generate-email")
def generate_email(request: EmailRequest):
    try:
        # Pass input as dict (required by CrewAI)
        result = email_crew.kickoff(inputs={"topic": request.topic})
        return {
            "topic": request.topic,
            "email": str(result)
        }
    except Exception as e:
        return {
            "error": str(e),
            "message": "Failed to generate email. Please try again."
        }
