from jira_connection import jira

def delete_issue(issue_key):
    jira.delete_issue(issue_key)