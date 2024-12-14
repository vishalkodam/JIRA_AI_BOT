from jira_connection import jira

def add_watcher(issue_key, watcher):
    return jira.add_watcher(issue_key, watcher)