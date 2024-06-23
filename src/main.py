import os
import time
import csv
from crewai import Crew
from langchain_groq import ChatGroq
from src.crew.agents import EmailPersonalizationAgents
from src.crew.tasks import PersonalizeEmailTask

# 0. Setup environment
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email template to be personalized
email_template = """
Hey [Name]!

Just a quick reminder that we have a Skool community where you can 
join us for weekly coaching calls every Tuesday at 6 PM Eastern time.
The community is completely free and we're about to hit the 500
user milestone. We'd love to have you join us!

If you have any questions or need help with your projects, 
this is a great place to connect with others and get support. 

If you're enjoying the AI-related content, make sure to check out 
some of the other videos on my channel. Don't forget to hit that 
like and subscribe button to stay updated with the latest content. 
Looking forward to seeing you in the community!

Best regards,
Aditya
"""

# 1. Create agents
agents = EmailPersonalizationAgents()

# Create email personalizer and ghostwriter agents
email_personalizer = agents.personalize_email_agent()
ghostwriter = agents.ghostwriter_agent()

# 2. Create tasks
tasks = PersonalizeEmailTask()

# Lists to store tasks
personalize_email_tasks = []
ghostwrite_email_tasks = []

# Function to start the email personalization process
def crew_starter(csv_file_path):
    # Open the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        # Create a CSV reader object
        csv_reader = csv.DictReader(file)

        # Iterate over each row in the CSV file
        for row in csv_reader:
            # Extract recipient information from each row
            recipient = {
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'email': row['email'],
                'bio': row['bio'],
                'last_conversation': row['last_conversation']
            }

            # Create a personalize_email task for each recipient
            personalize_email_task = tasks.personalize_email(
                agent=email_personalizer,
                recipient=recipient,
                email_template=email_template
            )

            # Create a ghostwrite_email task for each recipient
            ghostwrite_email_task = tasks.ghostwrite_email(
                agent=ghostwriter,
                draft_email=personalize_email_task,
                recipient=recipient
            )

            # Add tasks to their respective lists
            personalize_email_tasks.append(personalize_email_task)
            ghostwrite_email_tasks.append(ghostwrite_email_task)

    # Setup Crew
    crew = Crew(
        agents=[email_personalizer, ghostwriter],
        tasks=[*personalize_email_tasks, *ghostwrite_email_tasks],
        max_rpm=25
    )

    # Start the crew to execute tasks asynchronously
    results = crew.kickoff()

