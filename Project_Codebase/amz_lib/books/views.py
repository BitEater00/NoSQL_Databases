from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from books import datahandler as data
from django.core.paginator import Paginator
from django.contrib import messages

# Create your views here.


def home(request):
    # retreiveList = data.gethistory()
    # retreiveList.reverse()
    return render(request, 'index.html')


def loadbook(request, id=0):
    book = data.getBook(id)
    if request.user.is_authenticated:
        username = request.user.username
        if data.checkbookbookmarkedforuser(username, id):
            status = "bg-warning"
        else:
            status = "bg-info"
    else:
        status = "bg-info"
    context = {
        "book": book,
        "status": status
    }

    data.increasebookview(id)
    data.addtohistory(book['ASIN'], book['IMAGEURL'], book['TITLE'],
                      book['AUTHOR'], book['CATEGORYID'], book['CATEGORY'])
    return render(request, 'loadbook.html', context)


def books(request):
    allBooks = data.getAllBooks()
    paginator = Paginator(allBooks, 48)
    page_number = request.GET.get('page')
    page_object = paginator.get_page(page_number)

    return render(request, 'allbooks.html', {'page_object': page_object})


def bookmark(request, id):
    if request.user.is_authenticated:
        user = request.user.username
        if data.checkbookbookmarkedforuser(user, id):
            data.delbookmark(user, id)
            data.decreasebookmark(id)
            status = "bg-info"
            return redirect(request.META['HTTP_REFERER'], {"status": status})
        else:
            data.addBookmark(user, id)
            data.increasebookmark(id)
            status = "bg-warning"
            return redirect(request.META['HTTP_REFERER'], {"status": status})
    else:
        messages.error(request, 'Login to bookmark a book to your list')
        return redirect(request.META['HTTP_REFERER'])


def mybookmarks(request):
    if request.user.is_authenticated:
        username = request.user.username
        try:
            bookmarkedbooks = data.getbookmarksforuser(username)
            return render(request, 'mybookmarks.html', {'bookmarkedbooks': bookmarkedbooks})
        except:
            return HttpResponse('Returned None')
    return redirect(request.META['HTTP_REFERER'])


def addbook(request):
    if request.method == "POST":
        message = "There was some error on our side. Please wait while we resolve it."
        ASIN = request.POST['ASIN']
        IMAGE_URL = request.POST['IMAGEURL']
        TITLE = request.POST['TITLE']
        AUTHOR = request.POST['AUTHOR']
        CATEGORY_ID = request.POST['CATEGORYID']
        CATEGORY = request.POST['CATEGORY']
        alreadyexists = data.checkId(ASIN)
        if(alreadyexists):
            message = "This book already exists in our database.Thank you for your valuable time"
        else:
            additionstatus = data.addbookdb(
                ASIN, IMAGE_URL, TITLE, AUTHOR, CATEGORY_ID, CATEGORY)
            if(additionstatus):
                message = "Book info added our database.Thank you for your valuable time"
        context = {"message": message}
        return render(request, "addbooks.html", context)

    return render(request, "addbooks.html")


def deletebook(request):
    if request.method == "POST":
        if request.POST['action'] == "Load":
            ASIN = request.POST['ASIN']
            alreadyexists = data.checkId(ASIN)
            if(alreadyexists):
                book_details = data.getBook(ASIN)
                if book_details is not None:
                    context = {"books": [book_details]}
                else:
                    context = {"books": []}

                return render(request, "deletebook.html", context)
            else:
                return render(request, "deletebook.html", context={"books":  []})
        else:
            message = "There was some error on our side. Please wait while we resolve it."
            ASIN = request.POST['ASIN']
            alreadyexists = data.checkId(ASIN)
            if(alreadyexists):
                deletionstatus = data.deletebookdb(ASIN)
                if(deletionstatus):
                    message = "The book has been deleted from our database.Thank you for your time."
            else:
                message = "Book does not exits in our database. We will look forward to add it."

            context = {"message": message}
            return render(request, "deletebook.html", context)

    return render(request, "deletebook.html")


def updatebook(request):
    if request.method == "POST":
        if request.POST['action'] == "Load":
            ASIN = request.POST['ASIN']
            alreadyexists = data.checkId(ASIN)
            if(alreadyexists):
                book_details = data.getBook(ASIN)
                if book_details is not None:
                    context = book_details
                else:
                    context = {}

                return render(request, "updatebook.html", context)
            else:
                return render(request, "updatebook.html", context={})
        else:
            message = "There was some error on our side. Please wait while we resolve it."
            ASIN = request.POST.get('ASIN', "")
            IMAGE_URL = request.POST['IMAGEURL']
            TITLE = request.POST['TITLE']
            AUTHOR = request.POST['AUTHOR']
            CATEGORY_ID = request.POST['CATEGORYID']
            CATEGORY = request.POST['CATEGORY']
            alreadyexists = data.checkId(ASIN)
            if(alreadyexists):
                updatestatus = data.updatebookdb(
                    ASIN, IMAGE_URL, TITLE, AUTHOR, CATEGORY_ID, CATEGORY)
                if(updatestatus):
                    message = "This book details are updated in our database.Thank you for your valuable time"
                else:
                    message = "Book does not exits in our database. We will look forward to add it."

            context = {"message": message}
            return render(request, "updatebook.html", context)

    return render(request, "updatebook.html")
