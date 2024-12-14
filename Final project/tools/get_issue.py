from jira_connection import jira

def get_issue(issue_key):
    return jira.issue(issue_key)
