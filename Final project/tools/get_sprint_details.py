from jira_connection import jira

def get_sprint_details(sprint_id):
    return jira.get_sprint(sprint_id)