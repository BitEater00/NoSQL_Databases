from django.urls import path
from search import views

urlpatterns = [
    path("history/" , views.load_history),
    path("" , views.load_data),
]
