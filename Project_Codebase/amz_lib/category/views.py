from django.shortcuts import render
from django.http.response import HttpResponse
from category.models import AllCategories
from books import datahandler as data
from django.core.paginator import Paginator

# Create your views here.


def allCategories(request):
    allCategory = AllCategories.objects.all()
    return render(request, "allcategories.html", {'allcategory': allCategory})

def categories(request, id):
    bookByCategory = data.getbookforcategory(id)
    paginator = Paginator(bookByCategory, 48)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'category.html', {'page_object': page_object})