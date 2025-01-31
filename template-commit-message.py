#!/usr/bin/env python3

import subprocess

from langchain_ollama import ChatOllama
# Uncomment the following line to use Claude API
# from langchain_anthropic import ChatAnthropic
import os

client_ollama = ChatOllama(
    base_url=os.getenv("BASE_URL_AI"),
    model="qwen2.5-coder:3b",
    temperature=0.5,
)

# claude_client = ChatAnthropic(
#     api_key=os.getenv("CLAUDE_API_KEY"),
#     model="claude-3-5-sonnet-20240620",
# )


def get_git_diff():
    """Fetch the git changes."""
    result = subprocess.run(
        ["git", "diff", "--staged"], stdout=subprocess.PIPE, text=True
    )
    return result.stdout


def generate_commit_message(changes):
    """Use OpenAI API to generate a commit message."""
    prompt_message = [
        (
            "system",
            "You are an assistant that generates helpful and concise git commit messages.",
        ),
        (
            f"Generate a Git commit message for the following changes, following the Git commit standards:\n\n{changes}"
        ),
    ]
    # Uncomment the following line to use Claude API
    
    # response = claude_client.invoke(prompt_message)

    response = client_ollama.invoke(prompt_message)

    print(f"Response: {response.content}")
    return response.content


def main():
    # Fetch the changes
    changes = get_git_diff()

    if not changes:
        print("No staged changes found.")
        return

    # Generate commit message
    print(f"Changes: {changes}")
    commit_message = generate_commit_message(changes)
    print(f"Generated Commit Message: {commit_message}")

    # Optional: Automatically commit with the generated message
    subprocess.run(["git", "commit", "-m", commit_message])


if __name__ == "__main__":
    main()
