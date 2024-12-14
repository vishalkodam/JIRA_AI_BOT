from jira_connection import jira

def delete_board(board_id):
    jira.delete_board(board_id)