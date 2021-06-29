from pymongo import MongoClient
import pandas as pd  

def RepresentsInt(s):
    try: 
        int(s)
        return False
    except ValueError:
        return True
		
def checkAuthor(book):
	try:
		author = book['Author']
		return True
	except:
		return False
	
client = MongoClient(port = 27017)
db = client.Project
book_ASIN_list = []
books = db.Books.find({})
count = 0
for book in books:
	if len(book['ASIN']) < 9 or len(book['ASIN']) > 10 or checkAuthor(book):
		count = count +1
		print(book['ASIN'])
		book_ASIN_list.append(book['ASIN'])
	elif RepresentsInt(book['ASIN']):
		count = count+1
		print(book['ASIN'])
		book_ASIN_list.append(book['ASIN'])

print("Saving Started")
dict = {"ASIN" : book_ASIN_list}
df = pd.DataFrame(dict) 
df.to_csv('todel.csv') 
print("Saving Done")
print("\n\n\n\n")
print("count: ") 
print(count)