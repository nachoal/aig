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

def get_new_files():
    """
    Identifies new files in the Git repository.
    Returns a list of new file paths.
    """
    repo_path = get_repo_path()
    if not repo_path:
        print("Not in a Git repository.")
        return None

    repo = Repo(repo_path)
    new_files = [item.a_path for item in repo.index.diff('HEAD') if item.new_file]
    return new_files

def check_git_status():
    """
    Checks the status of the Git repository and returns modified files, new files, and their diffs.
    Returns None if no changes or not in a Git repo.
    """
    repo_path = get_repo_path()
    if not repo_path:
        print("Not in a Git repository.")
        return None

    repo = Repo(repo_path)
    changed_files = [item.a_path for item in repo.index.diff(None)]
    new_files = get_new_files()
    if not changed_files and not new_files:
        return None

    diffs = {}
    for file in changed_files:
        try:
            file_diff = repo.git.diff('HEAD', '--', file)
            diffs[file] = file_diff
        except GitCommandError as e:
            print(f"Error getting diff for {file}: {e}")

    return {"changed_files": diffs, "new_files": new_files}

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
