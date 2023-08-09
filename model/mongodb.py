from pymongo import MongoClient
import datetime
from bs4 import BeautifulSoup
import requests

# Authentication Database認證資料庫
stockDB='mydb'
dbname = 'howard-good31'

def constructor_stock(): 
    client = MongoClient("mongodb://yvesyu01:Yo0978175306@ac-znpydnf-shard-00-00.kyaqaqb.mongodb.net:27017,ac-znpydnf-shard-00-01.kyaqaqb.mongodb.net:27017,ac-znpydnf-shard-00-02.kyaqaqb.mongodb.net:27017/?ssl=true&replicaSet=atlas-11uzo2-shard-0&authSource=admin&retryWrites=true&w=majority")
    db = client[stockDB]
    return db

#----------------------------更新暫存的股票名稱--------------------------
def update_my_stock(user_name,  stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    collect.update_many({"favorite_stock": stockNumber }, {'$set': {'condition':condition , "price": target_price}})
    content = f"股票{stockNumber}更新成功"
    return content
#   -----------    新增使用者的股票       -------------
def write_my_stock(userID, user_name, stockNumber, condition , target_price):
    db=constructor_stock()
    collect = db[user_name]
    is_exit = collect.find_one({"favorite_stock": stockNumber})
    if is_exit != None :
        content = update_my_stock(user_name, stockNumber, condition , target_price)
        return content
    else:
        collect.insert_one({
                "userID": userID,
                "favorite_stock": stockNumber,
                "condition" :  condition,
                "price" : target_price,
                "tag": "stock",
                "date_info": datetime.datetime.now()
            })
        return f"{stockNumber}已新增至您的股票清單"








# #Authentication Database 認證資料庫
# stockDB ='mydb'
# dbname = 'howard-good31'

# def constructor_stock():
#     client = MongoClient('mongodb://yvesyu01:Yo0978175306@ac-znpydnf-shard-00-00.kyaqaqb.mongodb.net:27017,ac-znpydnf-shard-00-01.kyaqaqb.mongodb.net:27017,ac-znpydnf-shard-00-02.kyaqaqb.mongodb.net:27017/?ssl=true&replicaSet=atlas-11uzo2-shard-0&authSource=admin&retryWrites=true&w=majority')
#     db = client[stockDB]
#     return db
# # ---------------更新暫存的股票名稱-----------
# def update_my_stock(user_name, stockNumber , condition , target_price):
#     db = constructor_stock()
#     collect = db[user_name]
#     collect.update_many({"favorite_stock":stockNumber},{'$set':{'condition':condition,'price':target_price}})
#     content = f"股票{stockNumber}更新成功"
#     return content

# # ---------------新增使用者的股票-------------
# def write_my_stock(userID, user_name, stockNumber , condition , target_price):
#     db=constructor_stock()
#     collect = db[user_name]
#     is_exit = collect.find_one({'favorite_stock': stockNumber})
#     if is_exit != None:
#         content= update_my_stock(user_name, stockNumber , condition , target_price)
#         return content    
#     else :
#         collect.insert_one({
#             'userID':userID,
#             'favorite_stock':stockNumber,
#             'condition':condition,
#             'price':target_price,
#             'tag':'stock',
#             'date_info': datetime.datetime.now()
#         })
#         return f"{stockNumber}已新增至您的股票清單"