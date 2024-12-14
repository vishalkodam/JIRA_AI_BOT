from jira_connection import jira

def get_project_details(project_key):
    return jira.project(project_key)
