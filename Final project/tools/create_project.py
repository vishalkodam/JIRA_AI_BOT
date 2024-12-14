from jira_connection import jira

def create_project(project_key, name, lead):
    return jira.create_project(project_key, name, lead)