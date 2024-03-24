from pymongo.mongo_client import MongoClient
import pandas as pd
import json


uri = "mongodb+srv://savitkumarchugh:savitkumarchugh@cluster0.rju4pds.mongodb.net/"


client = MongoClient(uri)


DATABASE_NAME="card"
COLLECTION_NAME="credit_card"


df=pd.read_csv(r"notebooks\creditCardFraud_28011964_120214.csv")


json_record=list(json.loads(df.T.to_json()).values())


client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)