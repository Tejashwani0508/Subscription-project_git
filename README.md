# Subscription Management System

A FastAPI-based REST API for managing subscriptions with SQLite database. This project provides full CRUD (Create, Read, Update, Delete) operations for managing subscriptions.

## Project Structure

```
├── main.py           # FastAPI application and route definitions
├── models.py         # SQLAlchemy ORM models
├── schemas.py        # Pydantic request/response schemas
├── crud.py           # CRUD operation functions
├── database.py       # Database configuration and session management
├── requirements.txt  # Python dependencies
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd "Subscription project_git"
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Server

Start the FastAPI development server:

```bash
python main.py
```

Or using uvicorn directly:

```bash
uvicorn main:app --reload
```

The API will be available at: `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

## API Endpoints

### Subscriptions

#### Create a Subscription
- **Endpoint:** `POST /subscriptions`
- **Request Body:**
  ```json
  {
    "title": "Netflix",
    "cost": 15.99,
    "start_date": "2026-01-01",
    "end_date": "2027-01-01",
    "type": "Monthly",
    "autopay": true
  }
  ```
- **Response:** `201 Created` with subscription object

#### Get All Subscriptions
- **Endpoint:** `GET /subscriptions`
- **Query Parameters:**
  - `skip` (optional): Number of records to skip (default: 0)
  - `limit` (optional): Maximum number of records to return (default: 100)
- **Response:** `200 OK` with list of subscriptions

#### Get a Specific Subscription
- **Endpoint:** `GET /subscriptions/{subscription_id}`
- **Response:** `200 OK` with subscription object or `404 Not Found`

#### Update a Subscription
- **Endpoint:** `PUT /subscriptions/{subscription_id}`
- **Request Body:** (All fields optional)
  ```json
  {
    "title": "Netflix Premium",
    "cost": 19.99
  }
  ```
- **Response:** `200 OK` with updated subscription or `404 Not Found`

#### Delete a Subscription
- **Endpoint:** `DELETE /subscriptions/{subscription_id}`
- **Response:** `204 No Content` or `404 Not Found`

## Database Schema

### Subscriptions Table

| Field | Type | Description |
|-------|------|-------------|
| id | Integer | Primary key, auto-increment |
| title | String | Subscription title/name |
| cost | Float | Cost of the subscription |
| start_date | Date | Subscription start date |
| end_date | Date | Subscription end date |
| type | String | Type of subscription (e.g., Monthly, Yearly) |
| autopay | Boolean | Whether autopay is enabled (default: False) |

## Example Usage with cURL

### Create a subscription
```bash
curl -X POST "http://localhost:8000/subscriptions" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Spotify",
    "cost": 12.99,
    "start_date": "2026-03-01",
    "end_date": "2027-03-01",
    "type": "Monthly",
    "autopay": true
  }'
```

### Get all subscriptions
```bash
curl -X GET "http://localhost:8000/subscriptions"
```

### Get a specific subscription
```bash
curl -X GET "http://localhost:8000/subscriptions/1"
```

### Update a subscription
```bash
curl -X PUT "http://localhost:8000/subscriptions/1" \
  -H "Content-Type: application/json" \
  -d '{
    "cost": 14.99,
    "autopay": false
  }'
```

### Delete a subscription
```bash
curl -X DELETE "http://localhost:8000/subscriptions/1"
```

## Technologies Used

- **FastAPI** - Modern Python web framework for building APIs
- **SQLAlchemy** - SQL toolkit and ORM
- **SQLite** - Lightweight embedded database
- **Pydantic** - Data validation using Python type annotations
- **Uvicorn** - ASGI web server

## Development

To modify the system:

1. **Add fields to subscriptions:** Edit `models.py` and `schemas.py`
2. **Add new endpoints:** Edit `main.py` and add corresponding CRUD functions in `crud.py`
3. **Modify database:** Update `models.py` and run the server to auto-create tables

## Notes

- The database file (`subscription.db`) is created automatically in the project root when the server starts
- All dates should be in `YYYY-MM-DD` format
- The API returns appropriate HTTP status codes for all operations
- Full API documentation is available at `/docs` (Swagger) when the server is running
