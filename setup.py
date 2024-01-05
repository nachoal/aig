from setuptools import setup, find_packages

setup(
    name='aig',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'GitPython',  # For interacting with Git
        'requests',   # For OpenAI API calls
        'keyring'     # For secure storage of API key
    ],
    entry_points={
        'console_scripts': [
            'aig = aig.main:main',
        ],
    },
)
