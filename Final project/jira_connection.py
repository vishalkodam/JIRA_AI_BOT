import os
from dotenv import load_dotenv
from atlassian import Jira

# Load environment variables from .env file
load_dotenv()

# Retrieve credentials from environment variables
jira_url = os.getenv("JIRA_URL")
jira_username = os.getenv("JIRA_USERNAME")
jira_password = os.getenv("JIRA_API_TOKEN")

# Initialize Jira connection
jira = Jira(
    url=jira_url,
    username=jira_username,
    password=jira_password
)
