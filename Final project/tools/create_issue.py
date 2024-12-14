from jira_connection import jira

def create_issue(summary, description, issue_type='Task'):
    project_key = "My KARBAN Project"
    for project in jira.projects():
        print(project)
        if project_key.lower() in project["name"].lower():
            project_key_name = project["key"]
            break
    return jira.issue_create({
            'project': {'key': project_key_name},
            'summary': summary,
            'description': description,
            'issuetype': {'name': issue_type}
        }
    )

if __name__ == "__main__":
    project_key = "SCRUM project" 
    summary = "For testing"
    description = "For testing"
    create_issue(summary, description, issue_type='Task')
