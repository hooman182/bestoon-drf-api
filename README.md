# Expense Tracker API

This project is an **Expense Tracker API** built using **Django** and **Django REST Framework (DRF)**. It enables users to manage their expenses with categorized collections and secure authentication.

## Features

- **User Authentication**:
  - User registration, login, and logout.
  - JWT Token-based authentication.

- **Expense Management**:
  - Categorize expenses using collections and categories.
  - Add, update, delete, and view expenses.
  - Manage collections, each associated with a category.
  
- **API Endpoints**:
  - Full RESTful API for interacting with categories, collections, and expenses.
    
- **OpenAPI Documentation**:
  - Comprehensive API documentation is available at `/api/schema/`.
---

## Models

1. **Category**:
   - Represents a group of collections (e.g., "Food", "Travel").
   
2. **Collection**:
   - Related to a specific category.
   - Groups multiple expenses (e.g., "January Groceries" under the "Food" category).
   
3. **Expense**:
   - Related to a specific collection.
   - Represents an individual expense (e.g., "Buy Milk" in the "January Groceries" collection).

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/expense-tracker-api.git
   cd expense-tracker-api
   
2. Install dependencies using Pipenv:
   ```bash
   pipenv install
   pipenv shell
   
3. Apply database migrations:
   ```bash
   python manage.py migrate

4. Create a superuser (optional for admin access):
   ```bash
   python manage.py createsuperuser

5. Run the development server:
   ```bash
   python manage.py runserver



https://roadmap.sh/projects/expense-tracker-api
