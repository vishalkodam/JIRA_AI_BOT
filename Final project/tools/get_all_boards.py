from jira_connection import jira

def get_all_boards():
    return jira.get_all_boards()