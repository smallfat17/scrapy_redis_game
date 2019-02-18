# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# from pymongo import MongoClient
#
from pymongo import MongoClient
import pymysql

class Game3DmPipeline(object):

    def __init__(self):
        self.db = MongoClient('master').test
        self.db.authenticate('jmw','jmw123')
        self.collection = self.db.game

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item



class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('master','root','326..dd','game_pub_date')
        self.cursor = self.conn.cursor()
    def process_item(self,item,spider):
        sql = 'INSERT INTO GAME_BY_3DM (name,english_name,developer,publisher,pub_date,game_type,station,language,label) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        lis = (item['Cname'],item['Ename'],item['developer'],item['publisher'],item['pub_date'],item['game_type'],item['station'],item['lang'],item['label'])
        self.cursor.execute(sql,lis)
        self.conn.commit()
        return item



