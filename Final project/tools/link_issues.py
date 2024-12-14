from jira_connection import jira

def link_issues(issue_key_1, issue_key_2, link_type='Relates'):
    return jira.create_issue_link(issue_key_1, issue_key_2, link_type)