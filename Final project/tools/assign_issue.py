from jira_connection import jira

def assign_issue(issue_key, assignee):
    jira.assign_issue(issue_key, assignee)