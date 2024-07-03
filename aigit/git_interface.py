import os
import logging
from git import Repo, GitCommandError

def get_repo_path():
    """
    Gets the path of the current Git repository.
    Returns None if not in a Git repository.
    """
    try:
        repo = Repo('.', search_parent_directories=True)
        return repo.git.rev_parse("--show-toplevel")
    except GitCommandError:
        return None

def get_detailed_diff():
    """
    Gets a detailed diff of all changes in the repository.
    Returns a dictionary with file paths as keys and their full diff as values.
    """
    repo_path = get_repo_path()
    if not repo_path:
        logging.info("Not in a Git repository.")
        return None

    repo = Repo(repo_path)
    diffs = {}

    # Tracked files
    for item in repo.index.diff(None):
        diffs[item.a_path] = {
            'content': repo.git.diff('HEAD', '--', item.a_path),
            'status': 'modified'
        }

    # Untracked files
    for file in repo.untracked_files:
        try:
            with open(os.path.join(repo.working_tree_dir, file), 'r') as f:
                diffs[file] = {
                    'content': f.read(),
                    'status': 'new'
                }
        except IOError as e:
            logging.error(f"Error reading untracked file {file}: {e}")

    return diffs

def commit_changes(commit_message):
    """
    Commits changes in the Git repository with the provided commit message.
    """
    repo_path = get_repo_path()
    if not repo_path:
        print("Not in a Git repository.")
        return False

    repo = Repo(repo_path)
    try:
        repo.git.add(A=True)
        repo.index.commit(commit_message)
        return True
    except GitCommandError as e:
        print(f"Error committing changes: {e}")
        return False
