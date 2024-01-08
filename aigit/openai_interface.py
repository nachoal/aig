from openai import OpenAI

def generate_commit_message(diff_data, api_key):
    """
    Generates a commit message using OpenAI's GPT-4 32k based on the provided diff data.
    
    :param diff_data: Dictionary with file paths as keys and diffs as values.
    :param api_key: OpenAI API key.
    :return: Generated commit message or None if unable to generate.
    """
    prompt = prepare_prompt(diff_data)

    client = OpenAI(
        api_key=api_key,
    )

    data = {
        "messages": [
            {"role": "system", "content": """
            You are an expert level git commit message generator AI.
            You will be given a list of files and their diffs. 
            Your goal is to return the best commit message summary for the changes.
            REMEMBER TO: 
            - ONLY RETURN THE MESSAGE AND NOTHING ELSE.
            - USE PRESENT TENSE.
            - KEEP IT 50 CHARACTERS OR LESS.
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

def prepare_prompt(diff_data):
    """
    Prepares the prompt to send to OpenAI based on diff data.
    
    :param diff_data: Dictionary with file paths as keys and diffs as values.
    :return: Formatted prompt string.
    """
    prompt_lines = ["Generate a commit message for the following changes:"]
    for file, diff in diff_data.items():
        prompt_lines.append(f"File: {file}\nDiff:\n{diff}\n")

    return "\n".join(prompt_lines)