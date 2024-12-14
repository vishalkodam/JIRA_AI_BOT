from jira_connection import jira

def create_sprint(board_id, name, start_date, end_date):
    return jira.create_sprint(name, board_id, start_date, end_date)