from jira_connection import jira

def get_issue_transitions(issue_key):
    return jira.transitions(issue_key)