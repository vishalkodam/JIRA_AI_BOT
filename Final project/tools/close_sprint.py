from jira_connection import jira

def close_sprint(sprint_id):
    jira.update_sprint(sprint_id, state='closed')