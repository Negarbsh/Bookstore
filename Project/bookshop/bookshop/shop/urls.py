from django.urls import path
from shop import views

urlpatterns = [
    path("", views.home, name="home"),
	path('login', views.signin, name="login"),
	path('signup', views.signup, name="singup"),
    path('manage/add_book', views.add_book, name="add_book"),
	path('book/<int:book_id>', views.get_book, name="book"),
	path('all_books', views.get_all_books, name="books"),
	path('books', views.get_books, name="search"),
	
	# path('category/<int:id>', views.get_book_category, name="category"),
	# path('writer/<int:id>', views.get_writer, name = "writer"),
]