# Personal Finance Tracker Database Schema

## Tables

### categories
- id: integer, primary key, auto-increment
- name: text, required
- created_at: timestamp, default now()
- updated_at: timestamp, default now()

### expenses
- id: integer, primary key, auto-increment
- amount: numeric, required
- date: date, required
- description: text, optional
- category_id: integer, foreign key -> categories.id, required
- created_at: timestamp, default now()
- updated_at: timestamp, default now()
