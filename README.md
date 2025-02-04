# git-commit-automation

## Overview

This repository contains a script to automate the generation of Git commit messages using AI models. The script fetches the staged changes and generates a commit message based on those changes.

## Setup

### Prerequisites

- Python 3.8 or higher
- Git
- Virtual environment tool (optional but recommended)

### Installation

1. **Clone this repository:**

    ```sh
    git clone git@github.com:AbrahamTheCoder/git-commit-automation.git

    cd git-commit-automation
    ```

2. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Set up environment variables:**

    Ensure the OpenAI API Key is Set in Your Environment: Add the following line to your shell profile (e.g., .bash_profile, .zshrc, or .bashrc):

    ```sh
    export CLAUDE_API_KEY='your-claude-api-key'
    export BASE_URL_AI='your-base-url-ai'
    ```

    Replace `'your-claude-api-key'` and `'your-base-url-ai'` with your actual API key and base URL.

### Usage

1. **Making the Script Executable and Accessible:**

    To make the script executable and accessible from any directory, follow these steps:


    ```sh
    chmod +x /path/to/your/template-commit-message.py 
    ```


2. **Move the Script to a Directory in Your PATH:**

    ```sh
    sudo mv /path/to/your/template-commit-message.py /usr/local/bin/generate_commit_message
    ```

3. **Reload Your Profile:**

    ```sh
        source ~/.bash_profile  # or source ~/.zshrc or source ~/.bashrc
    ```

4. **Running the Script**

    Ensure you have staged changes by running:

    ```sh
        git add .
    ```

    Then execute your script from any directory:

    ```sh
        generate_commit_message
    ```


### Optional Configuration

- To use the Claude API instead of the default model, uncomment the relevant lines in [template-commit-message.py](http://_vscodecontentref_/2) and ensure the `CLAUDE_API_KEY` is set in the [.env](http://_vscodecontentref_/3) file.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](http://_vscodecontentref_/4) file for details.
