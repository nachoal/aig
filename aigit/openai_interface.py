from openai import OpenAI

def generate_commit_message(diff_data, new_files, api_key):
    """
    Generates a commit message using OpenAI's GPT-4 32k based on the provided diff data and new files.
    
    :param diff_data: Dictionary with file paths as keys and diffs as values.
    :param new_files: List of new file paths.
    :param api_key: OpenAI API key.
    :return: Generated commit message or None if unable to generate.
    """
    prompt = prepare_prompt(diff_data, new_files)

    client = OpenAI(
        api_key=api_key,
    )

    data = {
        "messages": [
            {"role": "system", "content": """
            You are an expert level git commit message generator AI.
            You will be given a list of files and their diffs. 
            Generate the best commit message summary for the changes, following these guidelines:
            - ONLY RETURN THE COMMIT MESSAGE.
            - USE PRESENT TENSE FOR CLARITY.
            - KEEP IT UNDER 50 CHARACTERS FOR BREVITY.
            - AVOID MENTIONING FILE NAMES; FOCUS ON THE NATURE OF THE CHANGE.
            - BE CONCISE BUT DESCRIPTIVE TO CLEARLY CONVEY THE CHANGE'S PURPOSE.
            """
             },
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }

    try:
        response = client.chat.completions.create(model="gpt-4-1106-preview", **data)
        commit_message = response.choices[0].message.content.strip()
        return commit_message
    except Exception as e:
        print(f"Error calling OpenAI API: {e}")
        return None

def prepare_prompt(diff_data, new_files):
    """
    Prepares the prompt to send to OpenAI based on diff data and new files.
    
    :param diff_data: Dictionary with file paths as keys and diffs as values.
    :param new_files: List of new file paths.
    :return: Formatted prompt string.
    """
    prompt_lines = ["Generate a commit message for the following changes:"]
    for file, diff in diff_data.items():
        prompt_lines.append(f"File: {file}\nDiff:\n{diff}\n")
    if new_files:
        prompt_lines.append("New files:")
        for file in new_files:
            prompt_lines.append(f"File: {file}\n")
    return "\n".join(prompt_lines)
    return "\n".join(prompt_lines)