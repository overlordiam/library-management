from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse, PlainTextResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, or_
from sqlalchemy.orm import selectinload
from datetime import datetime
import json
import os

from .database.database import get_db, init_db
from .database.models import Book

app = FastAPI()

# Templates
templates_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "templates")
templates = Jinja2Templates(directory=templates_dir)

# Add HEAD request handler for health checks
@app.head("/")
async def head():
    return PlainTextResponse("")

async def get_book_recommendations(db: AsyncSession, user_book: Book) -> list[Book]:
    # Create a search pattern based on the book's genre and title keywords
    search_terms = []
    
    # Add genre-based search
    if user_book.genre:
        search_terms.append(Book.genre.ilike(f"%{user_book.genre}%"))
    
    # Add title-based keyword search
    # Split the title into words and search for books with similar words
    title_words = [word for word in user_book.title.split() if len(word) > 3]
    for word in title_words:
        search_terms.append(Book.title.ilike(f"%{word}%"))
    
    # If we have search terms, find similar books
    if search_terms:
        result = await db.execute(
            select(Book)
            .where(
                or_(*search_terms),
                Book.id != user_book.id,  # Exclude the current book
                Book.is_available == True  # Only show available books
            )
            .limit(3)  # Limit to 3 recommendations
        )
        return result.scalars().all()
    return []

@app.on_event("startup")
async def startup_event():
    await init_db()

@app.get("/")
async def home(request: Request, db: AsyncSession = Depends(get_db)):
    # Get all books
    result = await db.execute(select(Book))
    books = result.scalars().all()
    
    # Get recommendations if there are any checked out books
    recommendations = []
    for book in books:
        if not book.is_available:
            recs = await get_book_recommendations(db, book)
            recommendations.extend(recs)
    
    # Remove duplicates while preserving order
    seen = set()
    recommendations = [x for x in recommendations if not (x.id in seen or seen.add(x.id))]
    
    return templates.TemplateResponse(
        "index.html", 
        {
            "request": request, 
            "books": books,
            "recommendations": recommendations[:3]  # Limit to top 3 recommendations
        }
    )

@app.post("/books/add")
async def add_book(
    title: str = Form(...),
    author: str = Form(...),
    isbn: str = Form(None),
    publication_year: int = Form(None),
    genre: str = Form(None),
    db: AsyncSession = Depends(get_db)
):
    book = Book(
        title=title,
        author=author,
        isbn=isbn,
        publication_year=publication_year,
        genre=genre
    )
    db.add(book)
    await db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/{book_id}/delete")
async def delete_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    await db.delete(book)
    await db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/{book_id}/update")
async def update_book(
    book_id: int,
    title: str = Form(...),
    author: str = Form(...),
    isbn: str = Form(None),
    publication_year: int = Form(None),
    genre: str = Form(None),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = title
    book.author = author
    book.isbn = isbn
    book.publication_year = publication_year
    book.genre = genre
    
    await db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/{book_id}/checkout")
async def checkout_book(
    book_id: int,
    borrower_name: str = Form(...),
    db: AsyncSession = Depends(get_db)
):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    if not book.is_available:
        raise HTTPException(status_code=400, detail="Book is already checked out")
    
    book.is_available = False
    book.borrower_name = borrower_name
    book.checkout_date = datetime.now()
    
    await db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.post("/books/{book_id}/checkin")
async def checkin_book(book_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Book).where(Book.id == book_id))
    book = result.scalar_one_or_none()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.is_available = True
    book.borrower_name = None
    book.checkout_date = None
    book.return_date = datetime.now()
    
    await db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/books/search")
async def search_books(
    request: Request,
    query: str,
    db: AsyncSession = Depends(get_db)
):
    search = f"%{query}%"
    result = await db.execute(
        select(Book).where(
            (Book.title.ilike(search)) |
            (Book.author.ilike(search)) |
            (Book.isbn.ilike(search))
        )
    )
    books = result.scalars().all()
    return templates.TemplateResponse(
        "index.html", {"request": request, "books": books, "search_query": query}
    ) 