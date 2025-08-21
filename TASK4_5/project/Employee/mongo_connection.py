from pymongo import MongoClient

MONGO_URI= " mongodb+srv://adminUser:EKTA1234@cluster0.nyeipx8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGO_URI)

db= client("emp_db")
collection = db("employee")