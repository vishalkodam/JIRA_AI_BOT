from jira_connection import jira

def get_issue_comments(issue_key):
    return jira.issue_comments(issue_key)