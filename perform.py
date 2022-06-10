#import pymongo
from pprint import pprint

### For Config ###
import  mongo_conn as mg

## Database name passed
db = mg.getConnData("mongo_dip")
## Collection or table name passed
my_collection = db["user"]

## Insert data into MongoDB
def writeData(data={}):
    result = my_collection.insert_one(patient_record)
    return result

## Get data from MongoDB
def getData():
    for item in my_collection.find():
        pprint(item)


patient_record = {
   "Name": "Test1",
   "Age": 47,
   "Sex": "M",
   "Blood pressure": [{"sys": 156}, {"dia": 82}],
   "Heart rate": 82
}
#writeData(patient_record)
getData()
