from jira_connection import jira

def update_issue_status(issue_key, status):
    jira.transition_issue(issue_key, status)
