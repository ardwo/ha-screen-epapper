# Project Overview

This project contains a set of Python scripts designed to take screenshots of a Home Assistant dashboard. The primary goal is to generate images suitable for display on an e-paper screen.

The scripts use the Playwright library to automate a Chromium browser, navigate to a specific Home Assistant dashboard URL, handle authentication, and save a screenshot. The project name `ha-screen-epapper` and the viewport dimensions used in the scripts (e.g., 800x400) strongly suggest the target is an e-paper display.

## Key Technologies

*   **Python**: The scripting language used for automation.
*   **Playwright**: A Python library for browser automation.
*   **Home Assistant**: The target application for screenshotting.

# Building and Running

## Installation

The project dependencies are listed in `requirements.txt`. They can be installed using pip:

```bash
pip install -r requirements.txt
```

Playwright also requires browsers to be installed. The first time you run a script, you might need to run the following command:

```bash
playwright install
```

## Running the Scripts

The project contains a Python script to take screenshots of a Home Assistant dashboard.

*   `test.py`: A simple script that navigates to the dashboard URL and takes a screenshot. It requires a hardcoded authentication token.

To run the script, execute it from your terminal:

```bash
python test.py
```

**Note:** The scripts contain hardcoded credentials and URLs. You will need to modify them to point to your own Home Assistant instance and use your own credentials.

# Development Conventions

*   The project uses `pytest`, which suggests that there is an intention to have automated tests.
*   The scripts are self-contained and can be run individually.
*   The code includes comments in Polish.
