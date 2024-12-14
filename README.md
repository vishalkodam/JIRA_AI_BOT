# JIRA Chatbot

This project is a JIRA Chatbot interface that integrates OpenAI's GPT-4 model with JIRA to interact with JIRA issues, projects, sprints, and more through various commands. It provides a web interface where users can input commands related to JIRA and receive responses based on their requests.

## Project Structure

```
/JIRA_AI_BOT
│
├── /tools                    # Contains individual tool scripts for interacting with JIRA
│   ├── create_issue.py        # Tool for creating JIRA issues
│   ├── get_issue.py           # Tool for retrieving JIRA issue details
│   ├── update_issue_status.py # Tool for updating issue status
│   ├── delete_issue.py        # Tool for deleting a JIRA issue
│   ├── add_comment.py         # Tool for adding comments to issues
│   ├── assign_issue.py        # Tool for assigning issues to users
│   ├── ...                    # Other JIRA-related tools (see the full list in the code)
│
├── .gitignore                # Git ignore file
├── main.py                   # The main script running the chatbot and web interface
├── .env                      # Environment variables file (see below for details)
├── requirements.txt          # Required Python dependencies
└── README.md                 # Project README file (this file)
```

## Installation

To get the project up and running locally, follow the steps below.

### 1. Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/vishalkodam/JIRA_AI_BOT.git
cd JIRA_AI_BOT
```

### 2. Set up a virtual environment

It's recommended to use a virtual environment to manage dependencies.

- For `venv` (Python 3.x):

```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

In the root of your project directory, create a `.env` file and add the following environment variables:

```bash
OPENAI_API_KEY=your_openai_api_key
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_PROJECT=your_project_name
JIRA_API_TOKEN=your_jira_api_token
JIRA_USERNAME=your_jira_username
JIRA_INSTANCE_URL=your_jira_instance_url
```

- **`OPENAI_API_KEY`**: Your OpenAI GPT-4 API key. You can obtain it from [OpenAI's platform](https://platform.openai.com/account/api-keys).
- **`LANGCHAIN_API_KEY`**: Your LangChain API key (if applicable).
- **`LANGCHAIN_PROJECT`**: The name of your LangChain project (if applicable).
- **`JIRA_API_TOKEN`**: Your Atlassian JIRA API token. You can generate it from [Atlassian's API tokens page](https://id.atlassian.com/manage-profile/security/api-tokens).
- **`JIRA_USERNAME`**: Your JIRA username (usually your email address).
- **`JIRA_INSTANCE_URL`**: The base URL for your JIRA instance (e.g., `https://your-instance.atlassian.net`).

Make sure to **never** commit the `.env` file to version control for security reasons. Add `.env` to your `.gitignore` file to prevent this.

### 5. Run the Application

Once everything is set up, you can run the chatbot application with:

```bash
streamlit run main.py
```

This will start the Streamlit web interface. You can then interact with the JIRA chatbot, which will respond to various commands related to JIRA tasks.

## How It Works

### `main.py`

- **Main script** that integrates the chatbot functionality with Streamlit for a user-friendly web interface.
- It loads the required environment variables, sets up the OpenAI and JIRA API connections, and then processes user input.
- The chatbot uses `ChatOpenAI` from LangChain for processing natural language queries and interacting with various JIRA tools through the LangChain agent.

### `tools/`

The `tools` folder contains individual Python scripts for interacting with different parts of the JIRA API. Each tool is a function that handles specific operations in JIRA, like creating issues, updating status, and more.

Some of the tools included are:

- **create_issue.py**: Creates a new JIRA issue.
- **get_issue.py**: Retrieves details of a specific JIRA issue.
- **update_issue_status.py**: Updates the status of a JIRA issue.
- **delete_issue.py**: Deletes a JIRA issue.
- **add_comment.py**: Adds comments to a JIRA issue.
- **assign_issue.py**: Assigns a JIRA issue to a specific user.
- **get_project_details.py**: Fetches details of a JIRA project.
- **get_all_boards.py**: Fetches all boards in JIRA.

Each tool script contains the logic to interact with JIRA and provide the necessary data or perform an action.

### `JiraToolkit` & `JiraAPIWrapper`

- **JiraToolkit**: This integrates LangChain with JIRA, providing various JIRA-related tools to the chatbot, like fetching issue details, creating issues, etc.
- **JiraAPIWrapper**: This wrapper helps manage API calls to JIRA, making the process easier to integrate with LangChain and the chatbot interface.

## Example Commands

Here are some example commands you can use in the Streamlit web interface:

- **Create an Issue**:  
  `"Create a new issue: Fix bug in login page"`
  
- **Get Issue Details**:  
  `"Get details for issue ABC-123"`
  
- **Update Issue Status**:  
  `"Update issue ABC-123 status to 'In Progress'"`
  
- **Add Comment to Issue**:  
  `"Add comment to issue ABC-123: 'Please review the latest changes.'"`

## Development

### Run Tests

To run tests (if applicable), ensure you're using the virtual environment and run:

```bash
pytest
```

### Contributing

If you'd like to contribute to this project, feel free to fork it and submit a pull request. Ensure you follow the same code style and conventions used in the project.
