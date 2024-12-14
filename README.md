# JIRA Chatbot Interface

This project is a chatbot interface that integrates with JIRA, using LangChain and various tools to interact with the JIRA API. The bot allows you to create, update, and manage JIRA issues, sprints, projects, and more, all through natural language commands.

## Features

- **Create, update, delete JIRA issues**: Manage JIRA issues from within the chatbot interface.
- **Search issues**: Perform JQL-based searches on issues in your JIRA instance.
- **Manage boards, sprints, and projects**: Create, delete, and fetch details about boards, sprints, and projects in JIRA.
- **Add comments, assign users, and manage watchers**: Perform operations on JIRA issues, such as adding comments, assigning issues to users, and adding/removing watchers.
- **Permissions management**: Fetch user permissions for JIRA operations.
  
## Tools Integrated

This chatbot integrates several JIRA tools through LangChain:

- **JIRA Issue Management**: Create, update, and delete issues, add comments, assign issues, and manage watchers.
- **JIRA Project & Board Management**: Fetch project details, create boards, and manage sprints.
- **JIRA Subtask Management**: Create subtasks under issues.
- **Search & Querying**: Search for issues using JQL, view issue transitions, and fetch issue comments.

## Requirements

- Python 3.7 or later
- JIRA API token
- OpenAI API key
- LangChain, Streamlit, Atlassian API, and other dependencies

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/JIRA_AI_BOT.git
   cd JIRA_AI_BOT
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with the following variables:

   ```bash
   OPENAI_API_KEY=your_openai_api_key
   LANGCHAIN_API_KEY=your_langchain_api_key
   LANGCHAIN_PROJECT=your_langchain_project
   JIRA_API_TOKEN=your_jira_api_token
   JIRA_USERNAME=your_jira_username
   JIRA_INSTANCE_URL=your_jira_instance_url
   ```

4. Run the Streamlit app:

   ```bash
   streamlit run app.py
   ```

   This will start a web interface where you can interact with the JIRA chatbot.

## Usage

Once the app is running, you will be able to:

1. **Login to JIRA**: Enter your JIRA URL, username, and API token in the sidebar to authenticate with your JIRA instance.
2. **Enter commands**: Use the chatbot interface to enter commands such as:
   - Create a JIRA issue: `Create a JIRA issue: Bug with login`
   - Search for issues: `Search for issues with status "To Do"`
   - Update an issue: `Update issue ABC-123 status to "In Progress"`
   - Assign an issue: `Assign issue ABC-123 to user john_doe`
3. **View results**: The chatbot will display the results of the command after execution.

## Available Commands

- **Create Issue**: `Create an issue: <summary>`
- **Update Issue**: `Update issue <issue_key> status to <status>`
- **Delete Issue**: `Delete issue <issue_key>`
- **Add Comment**: `Add comment to issue <issue_key>: <comment>`
- **Assign Issue**: `Assign issue <issue_key> to <username>`
- **Search Issues**: `Search for issues with <criteria>`
- **Create Project**: `Create project <project_key> with name <project_name>`
- **Create Sprint**: `Create sprint on board <board_id> with name <sprint_name>`
- **Add Watcher**: `Add watcher to issue <issue_key> with username <watcher_username>`
- **Get Project Details**: `Get project details for <project_key>`

## Example

Here’s an example interaction:

1. **User Input**:
   - Enter the following in the sidebar text area: `Create an issue: Bug with login`
2. **Output**:
   - The chatbot will create the issue in JIRA and display the result.

## Troubleshooting

- **Connection issues**: Ensure that your JIRA credentials and API token are correct.
- **Permissions issues**: Ensure that the API token has the necessary permissions for issue creation and management.
- **Missing dependencies**: Make sure all dependencies in `requirements.txt` are installed.

## Contributions

Feel free to fork this repository and make contributions. If you find any bugs or have suggestions for improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
