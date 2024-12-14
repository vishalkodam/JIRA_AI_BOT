from jira_connection import jira

def create_subtask(parent_issue_key, summary, description):
    return jira.issue_create({
        'fields': {
            'parent': {'key': parent_issue_key},
            'summary': summary,
            'description': description,
            'issuetype': {'name': 'Sub-task'}
        }
    })