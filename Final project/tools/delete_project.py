from jira_connection import jira

def delete_project(project_key):
    jira.delete_project(project_key)