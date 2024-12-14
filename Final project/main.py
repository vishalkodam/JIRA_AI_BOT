from langchain.chat_models import ChatOpenAI
from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain.agents import Tool
from langchain import hub
from langchain_community.utilities.jira import JiraAPIWrapper
from langchain_community.agent_toolkits.jira.toolkit import JiraToolkit
from tools.create_issue import create_issue
from tools.get_issue import get_issue
from tools.update_issue_status import update_issue_status
from tools.delete_issue import delete_issue
from tools.add_comment import add_comment
from tools.assign_issue import assign_issue
from tools.search_issues import search_issues
from tools.get_project_details import get_project_details
from tools.get_all_boards import get_all_boards
from tools.create_sprint import create_sprint
from tools.get_issue_comments import get_issue_comments
from tools.create_subtask import create_subtask
from tools.link_issues import link_issues
from tools.get_sprint_details import get_sprint_details
from tools.add_watcher import add_watcher
from tools.remove_watcher import remove_watcher
from tools.get_user_permissions import get_user_permissions
from tools.get_board_sprints import get_board_sprints
from tools.update_sprint import update_sprint
from tools.close_sprint import close_sprint
from tools.get_issue_transitions import get_issue_transitions
from tools.get_all_projects import get_all_projects
from tools.create_board import create_board
from tools.delete_board import delete_board
from tools.get_all_users import get_all_users
from tools.create_project import create_project
from tools.delete_project import delete_project
from tools.get_component_details import get_component_details
from tools.create_component import create_component
from tools.delete_component import delete_component
from dotenv import load_dotenv
import streamlit as st
import os
from jira_connection import jira
from atlassian import Jira
from langchain.globals import set_verbose, get_verbose

set_verbose(True)

is_verbose = get_verbose()
print(f"Verbose mode is {'enabled' if is_verbose else 'disabled'}.")


load_dotenv()

llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.0,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)
jira_tools = [
    Tool(
        name="Get Issue",
        func=get_issue,
        description="Fetches the details of a specific JIRA issue given the issue key."
    ),
    Tool(
        name="Update Issue Status",
        func=update_issue_status,
        description="Updates the status of a JIRA issue. Provide input as a dictionary with 'issue_key' and 'status'."
    ),
    Tool(
        name="Delete Issue",
        func=delete_issue,
        description="Deletes a JIRA issue given the issue key."
    ),
    Tool(
        name="Add Comment",
        func=add_comment,
        description="Adds a comment to a JIRA issue given the issue key and comment text."
    ),
    Tool(
        name="Assign Issue",
        func=assign_issue,
        description="Assigns a JIRA issue to a specific user given the issue key and assignee username."
    ),
    Tool(
        name="Search Issues",
        func=search_issues,
        description="Searches for JIRA issues using JQL."
    ),
    Tool(
        name="Get Project Details",
        func=get_project_details,
        description="Fetches details of a JIRA project given the project key."
    ),
    Tool(
        name="Get All Boards",
        func=get_all_boards,
        description="Fetches all boards available in JIRA."
    ),
    Tool(
        name="Create Sprint",
        func=create_sprint,
        description="Creates a new sprint on a specific board given the board ID, name, start date, and end date."
    ),
    Tool(
        name="Get Issue Comments",
        func=get_issue_comments,
        description="Fetches all comments from a specific JIRA issue given the issue key."
    ),
    Tool(
        name="Create Subtask",
        func=create_subtask,
        description="Creates a subtask under a specific JIRA issue given the parent issue key, summary, and description."
    ),
    Tool(
        name="Link Issues",
        func=link_issues,
        description="Links two JIRA issues given their issue keys and an optional link type."
    ),
    Tool(
        name="Get Sprint Details",
        func=get_sprint_details,
        description="Fetches details of a specific sprint given the sprint ID."
    ),
    Tool(
        name="Add Watcher",
        func=add_watcher,
        description="Adds a watcher to a specific JIRA issue given the issue key and watcher username."
    ),
    Tool(
        name="Remove Watcher",
        func=remove_watcher,
        description="Removes a watcher from a specific JIRA issue given the issue key and watcher username."
    ),
    Tool(
        name="Get User Permissions",
        func=get_user_permissions,
        description="Fetches the permissions for the current user."
    ),
    Tool(
        name="Get Board Sprints",
        func=get_board_sprints,
        description="Fetches all sprints for a specific board given the board ID."
    ),
    Tool(
        name="Update Sprint",
        func=update_sprint,
        description="Updates the details of a specific sprint given the sprint ID and optional new name or state."
    ),
    Tool(
        name="Close Sprint",
        func=close_sprint,
        description="Closes a specific sprint given the sprint ID."
    ),
    Tool(
        name="Get Issue Transitions",
        func=get_issue_transitions,
        description="Fetches all possible transitions for a specific JIRA issue given the issue key."
    ),
    Tool(
        name="Get All Projects",
        func=get_all_projects,
        description="Fetches all projects available in JIRA."
    ),
    Tool(
        name="Create Board",
        func=create_board,
        description="Creates a new board given the board name and project key."
    ),
    Tool(
        name="Delete Board",
        func=delete_board,
        description="Deletes a specific board given the board ID."
    ),
    Tool(
        name="Get All Users",
        func=get_all_users,
        description="Fetches all users available in JIRA."
    ),
    Tool(
        name="Create Project",
        func=create_project,
        description="Creates a new project in JIRA given the project key, name, and lead."
    ),
    Tool(
        name="Delete Project",
        func=delete_project,
        description="Deletes a specific project given the project key."
    ),
    Tool(
        name="Get Component Details",
        func=get_component_details,
        description="Fetches details of a specific project component given the component ID."
    ),
    Tool(
        name="Create Component",
        func=create_component,
        description="Creates a new component in a project given the project key and component name."
    ),
    Tool(
        name="Delete Component",
        func=delete_component,
        description="Deletes a specific component from a project given the component ID."
    )
]
jira = JiraAPIWrapper(
    jira_api_token=os.getenv("JIRA_API_TOKEN"),
    jira_cloud="True",
    jira_instance_url=os.getenv("JIRA_INSTANCE_URL"),
    jira_username=os.getenv("JIRA_USERNAME")
)
toolkit = JiraToolkit.from_jira_api_wrapper(jira)
tools = toolkit.get_tools()
jira_tools.extend(tools)
prompt = hub.pull("hwchase17/structured-chat-agent")

agent = create_structured_chat_agent(llm, jira_tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=jira_tools, verbose=True, handle_parsing_errors=False)


if __name__ == "__main__":
    load_dotenv()
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGSMITH_ENDPOINT"] = "https://api.smith.langchain.com"
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")  # Loaded from .env
    os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")  # Loaded from .env
    st.set_page_config(page_title="JIRA Chatbot UI", layout="wide")
    st.title("JIRA Chatbot Interface")
    
    st.sidebar.header("JIRA Login")

    jira_url = st.sidebar.text_input("JIRA URL", "https://your-jira-instance.atlassian.net")
    jira_username = st.sidebar.text_input("Username", "your-email@example.com")

    jira_password = os.getenv("JIRA_API_TOKEN")  # Loaded from .env if set

    if not jira_password:
        jira_password = st.sidebar.text_input("API Token", type="password")
        if jira_password:
            os.environ['JIRA_API_TOKEN'] = jira_password  # Set the environment variable

        try:
            jira = Jira(
                url=jira_url,
                username=jira_username,
                password=jira_password
            )
            st.sidebar.success("Connected to JIRA successfully!")
        except Exception as e:
            st.sidebar.error(f"Failed to connect to JIRA: {str(e)}")

    st.sidebar.header("JIRA Chatbot Commands")
    prompt = st.sidebar.text_area("Enter your command:")

    if st.sidebar.button("Run Command"):
        jira = Jira(
                url=jira_url,
                username=jira_username,
                password=jira_password
            )
        if jira is None:
            st.error("Please connect to JIRA first!")
        else:
            if "Create a issue" in prompt:
                summary = prompt.split(":")[-1]
                result = create_issue(summary, summary)
                st.success("Command executed successfully!")
                st.write(result)
            else:
                result = agent_executor.invoke({"input": prompt})
                st.success("Command executed successfully!")
                st.write(result)