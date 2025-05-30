# DTEAM - Django Developer Practical Test

Welcome! This test will help us see how you structure a Django project, work with various tools, and handle common tasks in web development. Follow the instructions step by step. Good luck!

## Requirements:

Follow PEP 8 and other style guidelines, use clear and concise commit messages and docstrings where needed, structure your project for readability and maintainability, optimize database access using Django’s built-in methods, and provide enough details in your README.

## Version Control System

1. Create a **public GitHub repository** for this practical test, for example: `DTEAM-django-practical-test`.
2. Put the text of this test (all instructions) into `README.md`.
3. For each task, create a **separate branch** (for example, `tasks/task-1`, `tasks/task-2`, etc.).
4. When you finish each task, **merge** that branch back into `main` but **do not delete** the original task branch.

## Python Virtual Environment

1. Use `pyenv` to manage the Python version. Create a file named `.python-version` in your repository to store the exact Python version.
2. Use `Poetry` to manage and store project dependencies. This will create a `pyproject.toml` file.
3. Update your `README.md` with clear instructions on how to set up and use pyenv and Poetry for this project.

---

# Tasks

## Task 1: Django Fundamentals

1. **Create a New Django Project**
   - Name it something like `CVProject`.
   - Use the Python version set up in Task 2 and the latest stable Django release.
   - Use **SQLite** as your database for now.

2. **Create an App and Model**
   - Create a Django app (for example, `main`).
   - Define a `CV` model with fields like `firstname`, `lastname`, `skills`, `projects`, `bio`, and `contacts`.
   - Organize the data in a way that feels efficient and logical.

3. **Load Initial Data with Fixtures**
   - Create a fixture that contains at least one sample `CV` instance.
   - Include instructions in `README.md` on how to load the fixture.

4. **List Page View and Template**
   - Implement a view for the main page (e.g., `/`) to display a list of CV entries.
   - Use any CSS library to style them nicely.
   - Ensure the data is retrieved from the database efficiently.

5. **Detail Page View**
   - Implement a detail view (e.g., `/cv/<id>/`) to show all data for a single CV.
   - Style it nicely and ensure efficient data retrieval.

6. **Tests**
   - Add basic tests for the list and detail views.
   - Update `README.md` with instructions on how to run these tests.

---

## Task 2: PDF Generation Basics

1. Choose and install any HTML-to-PDF generating library or tool.
2. Add a “Download PDF” button on the CV detail page that allows users to download the CV as a PDF.

---

## Task 3: REST API Fundamentals

1. Install **Django REST Framework (DRF)**.
2. Create CRUD endpoints for the CV model (create, retrieve, update, delete).
3. Add tests to verify that each CRUD action works correctly.

---

## Task 4: Middleware & Request Logging

1. **Create a `RequestLog` Model**
   - You can put this in the existing app or a new app (e.g., `audit`).
   - Include fields such as `timestamp`, `HTTP method`, `path`, and optionally other details like query string, remote IP, or logged-in user.

2. **Implement Logging Middleware**
   - Write a custom Django middleware class that intercepts each incoming request.
   - Create a `RequestLog` record in the database with the relevant request data.
   - Keep it efficient.

3. **Recent Requests Page**
   - Create a view (e.g., `/logs/`) showing the 10 most recent logged requests, sorted by timestamp descending.
   - Include a template that loops through these entries and displays their timestamp, method, and path.

4. **Test Logging**
   - Ensure your tests verify the logging functionality.

---

## Task 5: Template Context Processors

1. **Create `settings_context`**
   - Create a context processor that injects your entire Django settings into all templates.

2. **Settings Page**
   - Create a view (e.g., `/settings/`) that displays `DEBUG` and other settings values made available by the context processor.

---

## Task 6: Docker Basics

1. Use Docker Compose to containerize your project.
2. Switch the database from SQLite to PostgreSQL in Docker Compose.
3. Store all necessary environment variables (database credentials, etc.) in a `.env` file.

---

## Task 7: Celery Basics

1. Install and configure **Celery**, using Redis or RabbitMQ as the broker.
2. Add a Celery worker to your Docker Compose configuration.
3. On the CV detail page, add an email input field and a “Send PDF to Email” button to trigger a Celery task that emails the PDF.

---

## Task 8: OpenAI Basics

1. On the CV detail page, add a “Translate” button and a language selector.
2. Include these languages: Cornish, Manx, Breton, Inuktitut, Kalaallisut, Romani, Occitan, Ladino, Northern Sami, Upper Sorbian, Kashubian, Zazaki, Chuvash, Livonian, Tsakonian, Saramaccan, Bislama.
3. Hook this up to an OpenAI translation API or any other translation mechanism you prefer. The idea is to translate the CV content into the selected language.

---

## Task 9: Deployment

Deploy this project to DigitalOcean or any other VPS. (If you do not have a DigitalOcean account, you can use this referral link to create account with $200 on balance: [https://m.do.co/c/967939ea1e74](https://m.do.co/c/967939ea1e74))

---

## That’s it!

Complete each task thoroughly, commit your work following the branch-and-merge structure, and make sure your `README.md` clearly explains how to install, run, and test everything. We look forward to reviewing your submission!

**Thank you!**


# CV Management API

## Table of Contents

1. [Python Environment Setup](#python-environment-setup)  
2. [Database Setup & Fixture Data](#database-setup--fixture-data)  
3. [Running Tests](#running-tests)
4. [Docker Environment Setup](#docker-environment-setup)
5. [Email Configuration](#email-configuration)


## Python Environment Setup

This project uses `pyenv` and `poetry`.

1. Install pyenv and poetry  
   (follow official docs: https://github.com/pyenv/pyenv?tab=readme-ov-file#installation, https://python-poetry.org/docs/#installation)

2. Set the Python version:
```zsh
pyenv install 3.11.8
pyenv local 3.11.8
```

3. Install dependencies:
```zsh
poetry install
```

4. Activate the environment:
```zsh
poetry shell
```

---

Python version is defined in `.python-version`  
Dependencies are defined in `pyproject.toml` and locked in `poetry.lock`


## Database Setup & Fixture Data

1. Apply migrations:
```zsh
python manage.py makemigrations
python manage.py migrate
```

2. Load sample data:
```zsh
python manage.py loaddata updated_cv_fixtures.json
```

---


## Running Tests

This project uses `pytest` with Django integration for testing.  
Make sure your virtual environment is activated before running tests.

### Run all tests:
```bash
pytest
```

### Run tests from a specific file:
```bash
pytest tests/test_views.py
```

- Tests are located in the `tests/` folder at the project root.
- The test database will be created and destroyed automatically during test runs.


---


## Docker Environment Setup

Before starting the project, copy the example environment file:

```bash
cp .env.sample .env
```

Edit the `.env` file with your custom values:

```dotenv
USE_DOCKER=True               # Set to True if using Docker
POSTGRES_DB=your_db_name
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_HOST=postgres_db     # or localhost (if running without Docker)
POSTGRES_PORT=5432
```

To build and start the project:

```bash
docker-compose up --build
```

The project will be available at:

```
http://localhost:8000
```

---


## Email Configuration

The project uses SMTP to send emails with PDF attachments (e.g., CV export).
Before sending emails, set the email-related environment variables in your `.env` file.

```dotenv
EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
DEFAULT_FROM_EMAIL=your_email@gmail.com
```
> ⚠️ For Gmail, you must enable **2-Step Verification** and generate an **App Password**.


---
