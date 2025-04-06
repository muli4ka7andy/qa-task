# QA Automation Task

This repository contains automated tests for both UI and API validation. The project is built using **Playwright** for UI testing and **requests** for API testing.

The repository can be found at: [https://github.com/muli4ka7andy/qa-task](https://github.com/muli4ka7andy/qa-task)

## Table of Contents
- [Project Setup](#project-setup)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running Tests](#running-tests)
- [Test Architecture](#test-architecture)
- [Challenges Encountered](#challenges-encountered)
- [License](#license)

---

## Project Setup

### Prerequisites

Before setting up the project, ensure that the following tools are installed on your local machine:

- **Python 3.13** (this is the version required for this project)
- **Git** (for version control)
- **pip** (Python package manager)

### Installation

#### 1. Clone the repository

First, clone the repository to your local machine using the following command:
```bash
git clone https://github.com/muli4ka7andy/qa-task.git
cd qa-task
```
#### 2. Set up the virtual environment and install dependencies

Create a virtual environment:
```bash
python -m venv .venv
```
Activate the virtual environment:
On Windows:
```bash
.venv\Scripts\activate
```
On macOS/Linux:
```bash
source .venv/bin/activate
```
Install the required packages:
```bash
pip install -r requirements.txt
```
Install Playwright browsers:
```bash
playwright install
```

#### 3. Running Tests
Run all tests
```bash
pytest
```
Run only UI tests
```bash
pytest ui_tests/
```
Run only API tests
```bash
pytest api_tests/
```
Run a specific test
```bash
pytest ui_tests/test_file_upload.py
```

## Additional Documentation
### Test Architecture
The test suite is divided into two main parts:

## 1. UI Tests:

- These tests are written using the Playwright framework for testing the functionality of the web interface.

- The tests interact with various elements on the page (like buttons, forms, etc.) to simulate user behavior and validate responses from the website.

- We have organized locators and actions into separate files to keep the code modular and easier to maintain.

## 2. API Tests:

- These tests interact with a mock API (JSONPlaceholder) to verify the endpoints functionality.

- The API tests are written using the requests library to send HTTP requests and assert the responses.

- Each test corresponds to one of the CRUD operations (GET, POST, PUT/PATCH, DELETE).

## Challenges Encountered
During the development of this project, several challenges were encountered:

### 1. UI Testing with Drag-and-Drop:

- Initially, it was difficult to emulate a drag-and-drop file upload interaction using Playwright.

- This was resolved by simulating the drag-and-drop event manually, by programmatically creating a DataTransfer object and dispatching it to the drop zone.

### 2. Setting up Playwright Locators:

- Keeping locators separated from test scripts was an important decision to improve code reusability.

- Managing locators across multiple test files while ensuring proper test flow was a challenge.

### 3. API Response Validation:

- Ensuring that the response format was consistent across different endpoints (such as JSON response structure) required careful inspection of the API documentation and testing edge cases.
