# Personal Finance Tracker API

A backend REST API built with Flask and SQLite to track personal expenses by category.

This project allows users to:
- Create expense records
- View all expenses
- Delete expenses
- Manage categories

## Tech Stack
- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Postman (for API testing)

## Features
- Add expense (POST /expenses)
- View all expenses (GET /expenses)
- Delete expense (DELETE /expenses/<id>)
- Add category (POST /categories)

## How to Run Locally

1. Clone the repository  
2. Create a virtual environment  
3. Install dependencies:

```bash
pip install flask flask-sqlalchemy

personal-finance-tracker/
├── app.py
├── requirements.txt
├── venv/
└── README.md
