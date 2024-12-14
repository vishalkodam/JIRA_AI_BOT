from jira_connection import jira

def get_all_projects():
    return jira.get_all_projects()