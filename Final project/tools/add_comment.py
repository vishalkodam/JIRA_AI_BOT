from jira_connection import jira
from langchain.tools import tool

@tool
def add_comment(issue_key, comment):
    """
    issue_key : issue key to send
    comment : comment to sent
    """
    return jira.issue_add_comment(issue_key, comment)