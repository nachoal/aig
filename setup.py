from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='aigit',
    version='0.1.6',
    author='Ignacio Alonso',
    author_email='ignacio.alley@gmail.com',
    description='A CLI tool to automatically generate git commit messages using OpenAI GPT-4',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nachoal/aig',
    packages=find_packages(),
    install_requires=[
        'GitPython',  # For interacting with Git
        'openai',   # For OpenAI API calls
        'keyring',     # For secure storage of API key
        'instructor',
        'loguru',
        'tiktoken',
        'python-dotenv' # Clean this up, not needed for the package
    ],
    entry_points={
        'console_scripts': [
            'aig = aigit.main:main',
        ],
    },
     classifiers=[
        'Development Status :: 3 - Alpha',  # Change to '5 - Production/Stable' if applicable
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Version Control :: Git',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.6',
)
