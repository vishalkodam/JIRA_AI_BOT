from jira_connection import jira

def get_board_sprints(board_id):
    return jira.get_all_sprints(board_id)