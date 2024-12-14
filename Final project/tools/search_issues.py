from jira_connection import jira

def search_issues(jql):
    return jira.jql(jql)