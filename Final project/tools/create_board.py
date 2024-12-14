from jira_connection import jira

def create_board(board_name, project_key):
    return jira.create_board(board_name, project_key)