import keyring
import getpass

SERVICE_NAME = "AI_Git_Helper"

def store_api_key(api_key):
    """
    Stores the OpenAI API key securely in the system's keyring.
    
    :param api_key: The API key to be stored.
    """
    user = getpass.getuser()
    keyring.set_password(SERVICE_NAME, user, api_key)

def get_api_key():
    """
    Retrieves the OpenAI API key from the system's keyring.

    :return: The API key or None if not found.
    """
    user = getpass.getuser()
    return keyring.get_password(SERVICE_NAME, user)
