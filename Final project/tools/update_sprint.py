from jira_connection import jira

def update_sprint(sprint_id, name=None, state=None):
    jira.update_sprint(sprint_id, name=name, state=state)