import argparse
from .logger import log, setup_logger
from .git_interface import get_detailed_diff, commit_changes
from .openai_interface import generate_commit_groups
from .config_manager import get_api_key, store_api_key
from dotenv import load_dotenv

load_dotenv()

def main():
    # Parse arguments
    parser = argparse.ArgumentParser(description="AI-powered Git Helper")
    parser.add_argument('--config', action='store_true', help="Configure API Key")
    parser.add_argument('-y', '--yes', action='store_true', help="Auto commit without asking for confirmation")
    parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose logging")
    args = parser.parse_args()

    setup_logger(args.verbose)

    # Configure API Key
    if args.config:
        api_key = input("Enter your OpenAI API key: ")
        store_api_key(api_key)
        log.info("API Key stored securely.")
        return

    # Ensure API key is set
    api_key = get_api_key()
    if not api_key:
        log.info("API key not found. Please run 'aig --config' to set your API key.")
        return

    # Check git status and get diffs
    changes = get_detailed_diff()
    if not changes:
        log.info("No changes detected.")
        return
    
    commit_groups = generate_commit_groups(changes, api_key)
    if not commit_groups:
        log.error("Failed to generate commit groups.")
        return

    if not args.yes:
        print("Generated commit groups:")
        for i, commit in enumerate(commit_groups.commits, 1):
            print(f"{i}. {commit.message}")
            print(f"   Files: {', '.join(commit.files)}")
        confirm = input("Do you want to proceed with these commits? (y/n): ")
        if confirm.lower() != 'y':
            log.info("Commit process cancelled.")
            return

    for commit in commit_groups.commits:
        commit_changes(commit.message, commit.files)
        log.info(f"Committed: {commit.message}")

if __name__ == "__main__":
    main()
