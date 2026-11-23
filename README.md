# TaskTrail

## Description

TaskTrail is a web app for organizing projects and tasks. Each user
has their own projects, and each project has its own tasks. I'm
building it while learning web development with Python and Flask.

## Author

Charles Burrell

## Contact

- Email: [deltafront@gmail.com](mailto:deltafront@gmail.com)
- GitHub: [charles-burrell-3](https://github.com/charles-burrell-3)

## Installation
The following details how to install all of the prerequisites for this project:
* [Python](https://www.python.org/) (3.13)
* [Make](https://www.gnu.org/software/make/)
* [Git Command Line Client](https://git-scm.com/downloads)
* [UV](https://docs.astral.sh/uv/)
* [Terraform](https://www.hashicorp.com/en/products/terraform)
* Package Managers:
  * MacOS: [Homebrew](https://brew.sh/)
  * Windows:[Chocolatey](https://chocolatey.org/)
  * Linux: [Homebrew](https://brew.sh/)

### Package managers
#### MacOS
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
Here's what to expect:

- It explains what it's about to do, and asks you to press `Return` to
  continue.
- It asks for your password. Type it and press `Return`. Nothing shows as
  you type, which is normal.
- It may install Apple's **Command Line Tools** first. That can take a few
  minutes. Be patient and let it finish.
- At the very end, it prints a section called **Next steps**, with two
  lines to run so your Terminal can find Homebrew. **Copy and run those two
  lines.** They're easy to miss, and skipping them is the most common
  reason Homebrew "doesn't work" after installing.

When it's done, close Terminal completely and open a new one.

### Windows (PowerShell, Administrator)
```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = `
  [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString(
  'https://community.chocolatey.org/install.ps1'))
```
It prints a lot of text and finishes by telling you Chocolatey is ready.
When it's done, close PowerShell and open a new Administrator window.

### Python
#### macOS:
```bash
brew install python
brew install --cask visual-studio-code
```
#### Windows (PowerShell, Administrator):
```powershell
choco install python vscode -y
```
### UV
#### MacOS
```bash
brew install uv
```
#### Windows
```powershell
choco install uv -y
```

## Python dependencies
* [Ruff](https://docs.astral.sh/ruff/formatter/) - Code linter and formatter
* [PyTest](https://docs.pytest.org/en/stable/) - Python testing framework
* [PyTest-Cov](https://pypi.org/project/pytest-cov/) - Code coverage report for Pytest
* [Flask](https://flask.palletsprojects.com/en/stable/) - A lightweight WSGI web application framework


## Make Targets

| Command    | Purpose                                                    |
|------------|------------------------------------------------------------|
| `help`     | Prints out all available targets                           |
| `update`   | Locks any newly added dependencies and syncs them          |
| `hello`    | Runs the initial `hello.py` test script                    |
| `lint`     | Checks source code files for correct syntax and bug smells |
| `install`  | Installs all required Python dependencies                  |
| `test`     | Runs all tests  and opens test coverage report             |
| `coverage` | Opens the coverage report (when coverage has failed)       |
| `run`      | Runs the local dev server                                  |
