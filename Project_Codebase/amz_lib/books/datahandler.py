from pymongo import MongoClient
client = MongoClient(port=27017)
db = client.Project


def addbookdb(ASIN, IMAGE_URL, TITLE, AUTHOR, CATEGORY_ID, CATEGORY):
    try:
        db.Books.insert_one({"ASIN": ASIN, "IMAGEURL": IMAGE_URL, "TITLE": TITLE,
                             "AUTHOR": AUTHOR, "CATEGORYID": CATEGORY_ID, "CATEGORY": CATEGORY})
    except:
        return False
    return True


def deletebookdb(ASIN):
    try:
        db.Books.delete_one({"ASIN": ASIN})
        db.History.delete_many({"ASIN": ASIN})
        db.Bookmarks.delete_many({"ASIN": ASIN})
    except:
        return False
    return True


def updatebookdb(ASIN, IMAGE_URL, TITLE, AUTHOR, CATEGORY_ID, CATEGORY):
    try:
        filter = {"ASIN": ASIN}
        newvalues = {"$set": {"IMAGEURL": IMAGE_URL, "TITLE": TITLE,
                              "AUTHOR": AUTHOR, "CATEGORYID": CATEGORY_ID, "CATEGORY": CATEGORY}}
        db.Books.update_one(filter, newvalues)
    except:
        return False
    return True


def checkId(id):
    try:
        num = db.Books.find_one({'ASIN': id})
        if num != None:
            return True
        else:
            return False
    except:
        raise Exception()


def getBook(id):
    try:
        book = db.Books.find_one({'ASIN': id})
        if book is not None:
            return book
        else:
            return None
    except:
        return None


def getAllBooks():
    try:
        allBooks = list(db.Books.find())
        # print(allBooks)
        if allBooks is not None:
            return allBooks
        else:
            return None
    except:
        return None


def increasebookview(bookid):
    try:
        filter = {"ASIN": bookid}
        db.Books.update(filter, {"$inc": {"VISITS": 1}})
        return True
    except:
        return False


def increasebookmark(bookid):
    try:
        filter = {"ASIN": bookid}
        db.Books.update(filter, {"$inc": {"BOOKMARKS": 1}})
        return True
    except:
        return False


def decreasebookmark(bookid):
    try:
        filter = {"ASIN": bookid}
        db.Books.update(filter, {"$inc": {"BOOKMARKS": -1}})
        return True
    except:
        return False


def getbookforcategory(categoryid):
    try:
        filter = {"CATEGORYID": categoryid}
        books = list(db.Books.find(filter))
        return books
    except Exception:
        return None


def getbookvisitcount(bookid):
    try:
        filter = {"ASIN": bookid}
        bookvisitcount = db.Books.find(filter, {"VISITS": 1})
        return bookvisitcount
    except:
        return None


def getbookbookmarkcount(bookid):
    try:
        filter = {"ASIN": bookid}
        bookbookmarkcount = db.Books.find(filter, {"BOOKMARKS": 1})
        return bookbookmarkcount
    except:
        return None


def gettopbookfromvisit():
    try:
        allbooks = list(db.Books.find().sort("VISITS", -1).limit(48))
        return allbooks
    except:
        return None


def gettopbooksfrombookmarks():
    try:
        allbooks = list(db.Books.find().sort("BOOKMARKS", -1).limit(48))
        return allbooks
    except:
        return None


def addtohistory(ASIN, IMAGE_URL, TITLE, AUTHOR, CATEGORY_ID, CATEGORY):
    try:
        db.History.insert_one({"_id": ASIN, "ASIN": ASIN, "IMAGEURL": IMAGE_URL, "TITLE": TITLE,
                               "AUTHOR": AUTHOR, "CATEGORYID": CATEGORY_ID, "CATEGORY": CATEGORY})
        return True
    except:
        return False


def gethistory():
    try:
        allbooks = list(db.History.find().limit(15))
        return allbooks
    except:
        return None


def addBookmark(userid, bookid):
    try:
        db.Bookmarks.insert_one({"ASIN": bookid, "userId": userid})
        return True
    except:
        return False


def delbookmark(userid, bookid):
    try:
        db.Bookmarks.delete_one({"ASIN": bookid, "userId": userid})
        return True
    except:
        return False


def getbookmarksforuser(userid):
    try:
        books_list = list(db.Bookmarks.find(
            {"userId": userid}, {"_id": 0, "ASIN": 1}))
        booklist = []
        for asin in books_list:
            for key, val in asin.items():
                booklist.append(val)
        if len(booklist) == 0:
            return None
        else:
            return list(db.Books.find({"ASIN": {"$in": booklist}}))
    except:
        return None


def getbookmarkeduserforbooks(bookid):
    try:
        books = list(db.Bookmarks.find({"ASIN": bookid}))
        return books
    except:
        return None


def checkbookbookmarkedforuser(userid, bookid):
    try:
        book = list(db.Bookmarks.find_one({"ASIN": bookid, "userId": userid}))
        if len(book) == 0:
            return False
        else:
            return True
    except:
        return False