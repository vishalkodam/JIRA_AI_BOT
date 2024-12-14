from jira_connection import jira

def create_component(project_key, component_name):
    return jira.create_component(project_key, component_name)