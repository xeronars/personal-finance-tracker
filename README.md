# Personal Finance Tracker API

## Project Overview

Personal Finance Tracker is a RESTful backend API built with Flask and SQLite that helps users record, organize, and manage daily expenses by category. The project demonstrates core backend development skills including:

- Database modeling with SQLAlchemy  
- Full CRUD operations  
- REST API design  
- JSON request handling  
- API testing with Postman  

---

## Tech Stack

- Python  
- Flask  
- Flask-SQLAlchemy  
- SQLite  
- Postman (API testing)

---

## Features

- Add expense → `POST /expenses`  
- View all expenses → `GET /expenses`  
- View single expense → `GET /expenses/<id>`  
- Update expense → `PUT /expenses/<id>`  
- Delete expense → `DELETE /expenses/<id>`  
- Add category → `POST /categories`

---

## How to Run Locally

1. Clone the repository

```bash
git clone <your-repo-url>
cd personal-finance-tracker
Create virtual environment

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
Install dependencies

pip install flask flask-sqlalchemy
```

## Run the application
```bash
python app.py
```
API will run at:

http://127.0.0.1:5000

## Example API Usage

### Add Category
```bash
POST /categories

{
  "name": "Food"
}
```
### Add Expense
```bash
POST /expenses

{
  "amount": 12.5,
  "description": "Lunch",
  "category_id": 1
}
```

### View All Expenses
```bash
GET /expenses

Response:

[
  {
    "id": 1,
    "amount": 12.5,
    "description": "Lunch",
    "date": "2026-01-19",
    "category_id": 1
  }
]
```

### Delete Expense
```bash
DELETE /expenses/1
```

## Project Structure
```bash
personal-finance-tracker/
├── app.py
├── requirements.txt
├── venv/
└── README.md
```

## Future Improvements
- Monthly total spending endpoint

- User authentication

- Budget limits by category

- Frontend UI integration

Author
Trung – North Park University Student