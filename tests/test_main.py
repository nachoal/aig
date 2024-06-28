import unittest
from unittest.mock import patch, MagicMock
from aigit.main import main
from aigit.git_interface import get_new_files, check_git_status
from aigit.openai_interface import generate_commit_message

class TestGitInterface(unittest.TestCase):
    
    @patch('aigit.git_interface.Repo')
    def test_get_new_files(self, MockRepo):
        mock_repo = MockRepo.return_value
        mock_repo.index.diff.return_value = [MagicMock(a_path='new_file.txt', new_file=True)]
        new_files = get_new_files()
        self.assertEqual(new_files, ['new_file.txt'])

    @patch('aigit.git_interface.check_git_status')
    def test_check_git_status_with_new_files(self, mock_check_git_status):
        mock_check_git_status.return_value = {
            "changed_files": {"file1.txt": "diff"},
            "new_files": ["new_file.txt"]
        }
        status = check_git_status()
        self.assertIn("new_files", status)
        self.assertEqual(status["new_files"], ["new_file.txt"])

    @patch('aigit.openai_interface.generate_commit_message')
    def test_generate_commit_message(self, mock_generate_commit_message):
        diff_data = {"file1.txt": "diff"}
        new_files = ["new_file.txt"]
        api_key = "test_api_key"
        mock_generate_commit_message.return_value = "Test commit message"
        commit_message = generate_commit_message(diff_data, new_files, api_key)
        self.assertEqual(commit_message, "Test commit message")

if __name__ == '__main__':
    unittest.main()
