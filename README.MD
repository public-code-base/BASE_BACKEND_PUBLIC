# Project Setup Guide

This ReadMe document provides detailed steps for setting up a project. The following steps include changing folder names, initializing a Git repository, creating a Python virtual environment, testing files, and integrating the code with existing files.

## Table of Contents
1. [Change Folder Names](#change-folder-names)
2. [Initialize Git Repository](#initialize-git-repository)
3. [Create Python Virtual Environment](#create-python-virtual-environment)
4. [Test Your Script](#test-your-script)
5. [Create Your Own Program](#create-your-own-program)
6. [Integration](#integration)

---

## Step 1: Change Folder Names

### Description
This step will guide you through changing all instances of `BASE_BACKEND_PUBLIC` to your desired folder or repository name.

### Instructions
- Open the project folder.
- Press `CTRL+SHIFT+H` to open the search and replace dialog.
- Search for `BASE_BACKEND_PUBLIC` and replace it with your desired folder or repository name.

---

## Step 2: Initialize Git Repository

### Description
This step involves removing the existing `.git` folder and initializing a new Git repository.

### Instructions
#### On Windows (using GitBash):
`rm -rf .git`
`git init`
#### On Mac:
`rm -rf .git`
`git init`

---

## Step 3: Create Python Virtual Environment

### Description
Creating a Python virtual environment to manage dependencies.

### Instructions
#### On Windows:
`python -m venv venv`
To activate:
`.\venv\Scripts\Activate`
Install libraries:
`pip install -r requirements.txt `

#### On Mac:
`python3 -m venv venv`
To activate:
`source venv/bin/activate`
Install libraries:
`pip3 install -r requirements.txt `

---

## Step 4: Test Your Script

### Description
To ensure that the setup is successful, test `./playground/play1.py` to see if it prints 'Hello World'.

### Instructions
Run the following command:
`python ./playground/play1.py`

Output should be:
`Hello world`

---

## Step 5: Create Your Own Program

### Description
Create your own program folder and make sure to import `__init__.py`.

### Instructions
- Create a new folder, for example, `MyProgram`.
- Inside the folder, create a Python file and add your code.
- Make sure to include an `__init__.py` file in the folder to make it a Python package.

---

## Step 6: Integration

### Description
Integrate your code with `api.api_endpoints.py` and `initialize_main.py` to make the program work as a whole.

### Instructions
- Import your module in `api.api_endpoints.py`.
- Call your module's function in `initialize_main.py`.

---

By following these steps, you should be able to set up and run your project successfully. If you encounter any issues, please refer to the troubleshooting section or contact support.
