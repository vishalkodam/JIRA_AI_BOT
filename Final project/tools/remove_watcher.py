from jira_connection import jira

def remove_watcher(issue_key, watcher):
    return jira.remove_watcher(issue_key, watcher)