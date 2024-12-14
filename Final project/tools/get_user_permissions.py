from jira_connection import jira

def get_user_permissions():
    return jira.my_permissions()