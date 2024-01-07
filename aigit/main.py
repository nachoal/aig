import argparse
from .git_interface import check_git_status, commit_changes
from .openai_interface import generate_commit_message
from .config_manager import get_api_key, store_api_key

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="AI-powered Git Helper")
    parser.add_argument('--config', action='store_true', help="Configure API Key")
    parser.add_argument('-y', '--yes', action='store_true', help="Auto commit without asking for confirmation")
    args = parser.parse_args()

    # Configure API Key
    if args.config:
        api_key = input("Enter your OpenAI API key: ")
        store_api_key(api_key)
        print("API Key stored securely.")
        return

    # Ensure API key is set
    api_key = get_api_key()
    if not api_key:
        print("API key not found. Please run 'aig --config' to set your API key.")
        return

    # Check git status and get diffs
    diffs = check_git_status()
    if not diffs:
        print("No changes detected.")
        return

    # Generate commit message using OpenAI
    commit_message = generate_commit_message(diffs, api_key)
    if not commit_message:
        print("Failed to generate commit message.")
        return

    if not args.yes:
        print("Generated commit message: ", commit_message)
        confirm = input("Do you want to commit these changes? (y/n): ")
        if confirm.lower() != 'y':
            print("Commit cancelled.")
            return

    # Commit changes
    commit_changes(commit_message)
    print("Changes committed with message: ", commit_message)

if __name__ == "__main__":
    main()
