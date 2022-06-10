## Developed for MongoDB
## Developed on : 09-06-2022

import pymongo

### For Config  Define Constant for USERNAME,PASSWORD , HOST,PORT,AUTHENTICATION in config.py file then include this file ###
import  config as cf

try:
    if(cf.AUTHENTICATION):
        client = pymongo.MongoClient("mongodb://"+cf.USERNAME+":"+cf.PASSWORD+"@"+cf.HOST+":"+cf.PORT+"/")
    else:
        client = pymongo.MongoClient("mongodb://"+cf.HOST+":"+cf.PORT+"/")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect: %s" % e)

## Database name in parameter , connection object in return
def getConnData(dbName="mongo_dip"):
    db = client[dbName]
    return db