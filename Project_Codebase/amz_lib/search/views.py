from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render
from search import datahandler as data
from books import datahandler as booksdata

# Create your views here.
def load_data(request):
    try:
        if request.method == "POST":
            TITLE = request.POST['TITLE']
            AUTHOR = request.POST['AUTHOR']
            CATEGORY = request.POST['CATEGORY']

            if len(TITLE) == 0 and len(AUTHOR) == 0:
                return render(request,"search.html")
            
            if len(TITLE) == 0 and len(AUTHOR) != 0:
                books = data.getBooksforAuthor(AUTHOR,CATEGORY)
                return render(request,"search.html" , context = {"books" : books})
            
            if len(TITLE) != 0 and len(AUTHOR) == 0:
                books = data.getBooksforTitle(TITLE,CATEGORY)
                return render(request,"search.html" , context = {"books" : books})

            if len(TITLE) != 0 and len(AUTHOR) != 0:
                books = data.getBooksforTitleAuthor(TITLE,AUTHOR,CATEGORY)
                return render(request,"search.html" , context = {"books" : books})

    except:
        return render(request , "search.html")

    return render(request,"search.html")


def load_history(request):
    allbooks = booksdata.gethistory() 
    return render(request,"history.html" , {"books" : allbooks})