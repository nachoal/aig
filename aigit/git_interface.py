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

def check_git_status():
    """
    Checks the status of the Git repository and returns modified files and their diffs.
    Returns None if no changes or not in a Git repo.
    """
    repo_path = get_repo_path()
    if not repo_path:
        print("Not in a Git repository.")
        return None

    repo = Repo(repo_path)
    changed_files = [item.a_path for item in repo.index.diff(None)]
    if not changed_files:
        return None

    diffs = {}
    for file in changed_files:
        try:
            file_diff = repo.git.diff('HEAD', '--', file)
            diffs[file] = file_diff
        except GitCommandError as e:
            print(f"Error getting diff for {file}: {e}")

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
