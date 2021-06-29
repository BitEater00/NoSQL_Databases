from pymongo import MongoClient
import csv

client = MongoClient(port = 27017)
db = client.Project
books = list(db.Books.find({}))
count = 0
"""
print("Updating ASIN...")
for book in books:
	if(len(book["ASIN"]) == 9):
		filter = {"ASIN": book["ASIN"]}
		newASIN = "0" + book["ASIN"]
		updateASIN = {"$set": {"ASIN": newASIN}}
		db.Books.update_one(filter, updateASIN)
		count += 1
print(count, "ASIN updated")
"""

rows = []
# reading csv file
with open("todel.csv", 'r') as csvfile:
	# creating a csv reader object
	csvreader = csv.reader(csvfile)

	# extracting each data row one by one
	for row in csvreader:
		rows.append(row[1])

# retrieving ASIN numbers
for row in rows[1:]:
	db.Books.delete_one({"ASIN": row})
	print("Book deleted with ASIN: ", row)