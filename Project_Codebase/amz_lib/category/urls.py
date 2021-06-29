from django.urls import path
from category import views

urlpatterns = [
    path('<str:id>', views.categories),
    path('', views.allCategories)
]
