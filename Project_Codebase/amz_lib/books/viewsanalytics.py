from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from books import datahandler as data

# Create your views here.


def topBooksByVisits(request):
    booksByVisits = data.gettopbookfromvisit()
    return render(request, 'topbooksbyvisit.html', {'booksByVisits': booksByVisits})


def topBooksByBookmarks(request):
    booksByBookmarks = data.gettopbooksfrombookmarks()
    return render(request, 'topbooksbybookmark.html', {'booksByBookmarks': booksByBookmarks})
