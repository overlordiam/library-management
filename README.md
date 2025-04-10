# Library Management System

A lightweight, easy-to-use library management system built with FastAPI and SQLite.

## Features

- Add, edit, and delete books
- Check-in/check-out system with borrower tracking
- Search functionality by title, author, or ISBN
- Responsive UI with TailwindCSS
- Real-time updates

## Setup Instructions

1. Create a virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the application:

```bash
uvicorn app.main:app --reload
```

4. Open your browser and navigate to: `http://localhost:8000`

## Usage

### Adding Books

1. Fill out the "Add New Book" form at the top of the page
2. Required fields: Title, Author
3. Optional fields: ISBN, Publication Year, Genre

### Managing Books

- **Search**: Use the search bar to find books by title, author, or ISBN
- **Check Out**: Click "Check Out" and enter borrower's name
- **Check In**: Click "Check In" to mark a book as returned
- **Edit**: Click "Edit" to modify book details
- **Delete**: Click "Delete" to remove a book from the system

## Technical Details

- Backend: Python FastAPI
- Database: SQLite with SQLAlchemy
- Frontend: HTML + TailwindCSS
- Real-time interactions: HTMX

## Known Limitations

1. No user authentication system
2. In-memory SQLite database (data will be reset when server restarts)
3. No image upload functionality for book covers
4. No backup/restore functionality

## Future Enhancements

1. Add user authentication and roles (librarian, member)
2. Implement persistent database with PostgreSQL
3. Add book cover image upload
4. Add email notifications for due dates
5. Add barcode scanning for books
