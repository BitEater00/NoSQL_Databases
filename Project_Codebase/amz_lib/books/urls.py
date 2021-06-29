from django.urls import path
from books import views, viewsanalytics

urlpatterns = [
    path("", views.home, name="home"),
    path("books/", views.books, name="books"),
    path("books/add/", views.addbook),
    path("books/mybookmarks/", views.mybookmarks),
    path("books/delete/", views.deletebook),
    path("books/update/", views.updatebook),
    path("books/id/<str:id>", views.loadbook, name="loadbook"),
    path("books/<str:id>", views.bookmark, name="bookmark"),
    path("analytics/top-books-by-visits", viewsanalytics.topBooksByVisits),
    path("analytics/top-books-by-bookmarks",
         viewsanalytics.topBooksByBookmarks),
]
