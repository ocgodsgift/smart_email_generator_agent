from crewai import Task, Crew
from email_agent import email_agent

# Define task
generate_email_task = Task(
    description="Generate an email based on the input phrase or {topic} provided by the user.",
    expected_output="A well-structured professional email draft.",
    agent=email_agent
)

# Define crew
email_crew = Crew(
    agents=[email_agent],
    tasks=[generate_email_task],
    verbose=True
)

# result = email_crew.kickoff(inputs={"topic": "write a resignation mail for me to ABC Company"})
# print(result)
