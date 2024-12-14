from jira_connection import jira

def get_component_details(component_id):
    return jira.get_component(component_id)