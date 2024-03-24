from datetime import datetime
import os

MONGO_DATABASE_NAME = "credit-card"
MONGO_COLLECTION_NAME = "card"
MONGO_DB_URL =  "mongodb+srv://savitkumarchugh:savitkumarchugh@cluster0.rju4pds.mongodb.net/"

TARGET_COLUMN = "default payment next month"

MODEL_FILE_NAME = "model"
MODEL_FILE_EXTENSION = ".pkl"

artifact_folder = "artifacts"