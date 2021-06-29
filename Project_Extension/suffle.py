from pymongo import MongoClient
import pandas as pd

client = MongoClient(port = 27017)
db = client.Project
books = db.Books.find({} , {"_id":0})
df = pd.DataFrame(books)
df.to_csv('updatedDataset.csv') 

