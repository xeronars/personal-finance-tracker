# Personal Finance Tracker API

## Project Overview

Personal Finance Tracker is a RESTful backend API built with Flask and SQLite that helps users record, organize, and manage daily expenses by category. The project demonstrates backend development skills including database modeling, CRUD operations, and API testing.


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

## Example API Usage

### Add Expense
POST /expenses  
Body (JSON):

```json
{
  "amount": 12.5,
  "description": "Lunch",
  "date": "2026-01-19",
  "category_id": 1
}

```bash
pip install flask flask-sqlalchemy

personal-finance-tracker/
├── app.py
├── requirements.txt
├── venv/
└── README.md
