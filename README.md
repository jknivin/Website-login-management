# Flask Setup

## Installation

### Linux

```bash
python -m venv env
source env/bin/activate
pip install Flask

``` short 

### Windows

```powershell
python -m venv env
env/Scripts/Activate.ps1
pip install Flask
```

### If you want to use powershell you can use this command:

Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

### Create a File called .py

like this: `main.py`

### Run it

```
python main.py

```

 Git: A version control system to track changes in source code during software development.
    GitHub: A web-based platform to host Git repositories, collaborate with others, and manage projects.

Setting Up Git 

    Install Git:
        Windows: Git for Windows
        macOS: brew install git
        Linux: sudo apt-get install git
    Configure Git:

    sh

    git config --global user.name "Your Name"
    git config --global user.email "your.email@example.com"

Basic Git Commands

    Initialize a Repository:

    sh

git init

Clone a Repository:

sh

git clone <repository-url>

Check Status:

sh

git status

Add Changes:

sh

git add <file-name>
git add . # To add all changes

Commit Changes:

sh

git commit -m "Commit message"

View Commit History:

sh

git log

Push to Remote Repository:

sh

git push origin main

Pull from Remote Repository:

sh

    git pull origin main

GitHub Basics 

    Create a GitHub Account:
        Sign up at GitHub.
    Create a Repository:
        Click on the "New" button on the GitHub dashboard.
        Fill in the repository name and description.
        Choose to make it public or private.
        Click "Create repository".
    Link Local Repository to GitHub:

    sh

    git remote add origin <repository-url>
    git push -u origin main

    Collaborating on GitHub:
        Forking: Create your own copy of someone else's repository.
        Pull Requests: Propose changes to a repository.
        Issues: Track bugs and feature requests.

Quick Project Example 

    Create a Simple Project:

    sh

    mkdir my-project
    cd my-project
    git init
    echo "# My Project" > README.md
    git add README.md
    git commit -m "Initial commit"
    git remote add origin <repository-url>
    git push -u origin main

    Collaboration:
        Invite collaborators via GitHub.
        Collaborators clone the repository, make changes, commit, and push.

