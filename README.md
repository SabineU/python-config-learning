# Python Configuration Learning

A hands-on project for learning Python application configuration, environment variables, dependency management, and Git.

## Project Contents

- `config/appsettings.json` — example application settings.
- `config_demo.py` — loads and validates environment-based configuration.
- `requirements.txt` — records the Python package versions used by the project.
- `.gitignore` — excludes local virtual environments, environment files, and Python-generated files.

## Prerequisites

- Python 3.14 or a compatible Python version.
- pip.
- A terminal such as PowerShell.

## Setup

Create and activate a virtual environment:

```powershell
py -3.14 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
python -m pip install -r requirements.txt
```

## Configuration

Create a local `.env` file containing the required settings:

```text
APP_MODE=development
API_BASE_URL=https://api.example.com
TIMEOUT_SECONDS=10
```

The application accepts `development`, `testing`, or `production` as application modes. The API base URL must use HTTP or HTTPS and include a hostname. The timeout must be a positive integer.

## Run

```powershell
python config_demo.py
```

The example validates the configuration and prints the selected application mode, API base URL, and timeout.

**Security:** Do not commit real credentials, API keys, tokens, or other secrets. The `.env` file is intended to remain local.
