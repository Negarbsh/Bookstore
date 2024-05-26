import jwt
from .utils.decorators import log_error
from .utils.hash import hash
from .models import User, Book


@log_error
def authenticate_user(username, password):
    if not username or not password:
        return None
    user = User.objects.get(username = username)
    if user is None:
        return None
    hashed_password = hash(password)
    if user.password_hash != hashed_password:
        return None
    return  {"token": jwt.encode({}, 'secret', algorithm='HS256'), "user": user}


@log_error
def signup(username, password, phone):
    if not username or not password or not phone:
        return None

    if len(phone) != 11:
        return None

    prv = User.objects.filter(username=username).exists() 
    if prv:
        return "Username exists"

    password_hash = hash(password)
    user = User(
        username = username, 
        password_hash = password_hash,
        phone = phone
    )

    user.save()
    return user


@log_error
def add_book(name, author, price, description, genre):
    prv = Book.objects.filter(name=name).exists() 
    if prv:
        return "Bookname exists"
    book = Book(name=name, author=author, price=price, description=description, genre=genre)
    book.save()
    return book


@log_error
def get_book(book_id):
    exists = Book.objects.filter(bookid=book_id).exists() 
    if not exists:
        return None
    
    book = Book.objects.get(bookid=book_id)
    return book


@log_error
def get_all_books():
    books = Book.objects.all()
    ans = []
    for book in books:
        ans.append({
            "name": book.name,
            "book_id": book.bookid,
            "author": book.author,
            "description": book.description,
            "genre": book.genre,
            "price": book.price
        })
    return ans