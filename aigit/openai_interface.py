from aigit.logger import log
from openai import OpenAI
import instructor
from instructor import OpenAISchema
from typing import List
from pydantic import Field

class Commit(OpenAISchema):
    message: str = Field(..., description="The commit message")
    files: List[str] = Field(..., description="List of files included in this commit")

class CommitGroups(OpenAISchema):
    commits: List[Commit] = Field(..., description="List of logically grouped commits")

def generate_commit_groups(diff_data, api_key):
    """
    Generates logically grouped commits using OpenAI's GPT-4 based on the provided diff data.
    
    :param diff_data: Dictionary with file paths as keys and values as another dict containing 'content' and 'status'.
    :param api_key: OpenAI API key.
    :return: CommitGroups object or None if unable to generate.
    """
    prompt = prepare_prompt(diff_data)

    client = OpenAI(api_key=api_key)
    client = instructor.patch(client)

    try:
        log.info("Sending request to OpenAI API")
        commit_groups = client.chat.completions.create(
            model="gpt-4-turbo",
            response_model=CommitGroups,
            messages=[
                {"role": "system", "content": """
                You are an expert level git commit message generator AI.
                Analyze the changes and group them logically into separate commits.
                Follow these guidelines:
                - Group related changes together.
                - Use present tense for commit messages.
                - Keep commit messages under 50 characters.
                - Be concise but descriptive to clearly convey the change's purpose.
                """},
                {"role": "user", "content": prompt}
            ],
            max_tokens=2000,
            temperature=0.7
        )
        log.debug(f"Received commit groups from OpenAI: {commit_groups}")
        return commit_groups
    except Exception as e:
        log.error(f"Error calling OpenAI API: {e}")
        return None

def prepare_prompt(diff_data):
    """
    Prepares the prompt to send to OpenAI based on diff data.
    
    :param diff_data: Dictionary with file paths as keys and values as another dict containing 'content' and 'status'.
    :return: Formatted prompt string.
    """
    prompt_lines = ["Analyze the following changes and group them into logical commits:"]
    for file, info in diff_data.items():
        status_line = f"{'New file' if info['status'] == 'new' else 'Diff'}: {file}"
        prompt_lines.append(f"{status_line}\nContent:\n{info['content']}\n")

    return "\n".join(prompt_lines)