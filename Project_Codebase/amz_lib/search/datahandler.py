from pymongo import MongoClient
client = MongoClient(port=27017)
db= client.Project

def getBooksforAuthor(AUTHOR,CATEGORY):
    try:
        if CATEGORY == "-1":
            books = db.Books.find({"AUTHOR" : { "$regex" :".*" + AUTHOR + ".*"}})
        else:
            books = db.Books.find({"AUTHOR" : { "$regex" :".*" + AUTHOR + ".*"} , "CATEGORYID" : CATEGORY})
        return books
    except:
        return None

def getBooksforTitle(TITLE,CATEGORY):
    try:
        if CATEGORY == "-1":
            books = db.Books.find({"TITLE" : { "$regex" :".*" + TITLE + ".*"}})
        else:
            books = db.Books.find({"TITLE" : { "$regex" :".*" + TITLE + ".*"} , "CATEGORYID" : CATEGORY})
        return books
    except:
        return None

def getBooksforTitleAuthor(TITLE,AUTHOR,CATEGORY):
    try:
        if CATEGORY == "-1":
            books = db.Books.find({"AUTHOR" : { "$regex" :".*" + AUTHOR + ".*"} , "TITLE" : { "$regex" :".*" + TITLE + ".*"}})
        else:
            books = db.Books.find({"AUTHOR" : { "$regex" :".*" + AUTHOR + ".*"} , "TITLE" : { "$regex" :".*" + TITLE + ".*"} , "CATEGORYID" : CATEGORY})
        return books
    except:
        return None
