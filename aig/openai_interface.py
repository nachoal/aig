import requests

def generate_commit_message(diff_data, api_key):
    """
    Generates a commit message using OpenAI's GPT-4 based on the provided diff data.
    
    :param diff_data: Dictionary with file paths as keys and diffs as values.
    :param api_key: OpenAI API key.
    :return: Generated commit message or None if unable to generate.
    """
    # Prepare the prompt
    prompt = prepare_prompt(diff_data)

    # OpenAI API URL
    api_url = "https://api.openai.com/v1/engines/davinci-codex/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    data = {
        "prompt": prompt,
        "max_tokens": 150,
        "temperature": 0.7
    }

    try:
        response = requests.post(api_url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        commit_message = result.get("choices", [{}])[0].get("text", "").strip()
        return commit_message
    except requests.RequestException as e:
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
