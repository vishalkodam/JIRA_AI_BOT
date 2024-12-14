from jira_connection import jira

def delete_component(component_id):
    jira.delete_component(component_id)