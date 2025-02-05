
from pymongo import MongoClient
import urllib.parse

# Properly encode username and password
username = urllib.parse.quote_plus("bazeer33333")  # Encodes special characters if present
password = urllib.parse.quote_plus("bazeer33333")  # Encodes special characters if present

# Correct MongoDB URI format
uri = f"mongodb+srv://{username}:{password}@cluster0.hhkh8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print("Error:", e)
