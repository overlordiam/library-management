# 📚 Library Management System

A modern, user-friendly library management system built with FastAPI and SQLite. Perfect for small libraries, book clubs, or personal collections.

![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104.1-green.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-blue.svg)

## ✨ Features

### 📖 Core Features

- **Book Management**
  - Add new books with title, author, ISBN, publication year, and genre
  - Edit existing book details
  - Remove books from the collection
  - View all books in an elegant grid layout

### 📱 User Experience

- **Modern Interface**
  - Clean, responsive design
  - Book-themed color scheme
  - Easy-to-use forms and buttons
  - Mobile-friendly layout

### 🔍 Search & Discovery

- **Smart Search**
  - Search by title, author, or ISBN
  - Real-time search results
  - Clear search functionality

### 📊 Book Status

- **Check-in/Check-out System**
  - Mark books as available or checked out
  - Track borrower information
  - Record checkout dates
  - Easy check-in process

### 🤖 AI-Powered Recommendations

- **Smart Book Suggestions**
  - Get recommendations based on checked-out books
  - Recommendations consider:
    - Similar genres
    - Related titles
    - Only shows available books
  - Up to 3 personalized suggestions

## 🚀 Quick Start

### Prerequisites

- Python 3.11 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd library-management-system
   ```

2. **Create a virtual environment**

   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   uvicorn app.main:app --reload
   ```

5. **Access the application**
   - Open your browser and navigate to: `http://localhost:8000`
   - The system is ready to use!

## 💡 Usage Guide

### Adding Books

1. Fill out the "Add New Book" form at the top
2. Required fields:
   - Title
   - Author
3. Optional fields:
   - ISBN
   - Publication Year
   - Genre

### Managing Books

- **Search**: Use the search bar to find books by title, author, or ISBN
- **Check Out**:
  1. Click "Check Out" on an available book
  2. Enter borrower's name in the popup
  3. Confirm checkout
- **Check In**: Click "Check In" on a checked-out book
- **Edit**: Update book details using the edit button
- **Delete**: Remove books from the system

### Book Recommendations

- Recommendations appear automatically when:
  - Books are checked out
  - Similar books are available
- Based on:
  - Genre matching
  - Title similarity
  - Current availability

## 🌐 Deployment

### Deploying to Render.com

1. Fork/push the repository to GitHub
2. Create a new Web Service on Render
3. Connect your GitHub repository
4. Use these settings:
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}`
   - Environment Variables:
     - `PYTHON_VERSION`: `3.11.0`

### Port Configuration

- The application binds to `0.0.0.0` to serve HTTP requests
- Uses Render's `PORT` environment variable (defaults to 10000 if not set)
- Production-ready configuration without development flags
- Automatic HTTPS handling by Render's load balancer

### Important Notes

1. **Development vs Production**

   - Local development uses: `uvicorn app.main:app --reload`
   - Production (Render) uses: `uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-10000}`

2. **SSL/HTTPS**

   - Render handles SSL termination automatically
   - Your app will be available via HTTPS
   - HTTP requests are automatically redirected to HTTPS

3. **Troubleshooting**
   - If deployment fails, check the logs for port binding issues
   - Ensure the app is not binding to `127.0.0.1` in production
   - Avoid using Render's reserved ports (18012, 18013, 19099)

## 🔧 Technical Details

### Stack

- **Backend**: Python FastAPI
- **Database**: SQLite with SQLAlchemy
- **Frontend**:
  - HTML with Jinja2 Templates
  - TailwindCSS for styling
  - Vanilla JavaScript for interactions

### Database Schema

- Books table with fields:
  - id (Primary Key)
  - title
  - author
  - isbn (Optional)
  - publication_year (Optional)
  - genre (Optional)
  - is_available (Boolean)
  - borrower_name
  - checkout_date
  - return_date

## 📝 Known Limitations

1. Data persistence:
   - Uses SQLite (resets on server restart)
   - Consider upgrading to PostgreSQL for production
2. Authentication:
   - No user authentication system
   - Single user environment
3. Features:
   - No image upload for book covers
   - No barcode scanning
   - No email notifications

## 🔜 Future Enhancements

1. User authentication and roles
2. Persistent database with PostgreSQL
3. Book cover image upload
4. Email notifications for due dates
5. Barcode scanning for books
6. Export/import functionality
7. Advanced statistics and reports

## 🤝 Contributing

Feel free to:

- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.
