# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings
from datetime import datetime

class ImdbPipeline(object):
    """Stores the given items in the movies MongoDB collection"""
    def __init__(self):
    	"""This function sets the connection to mongodb and binds the collection varable to the actual db collection"""
    	conn = MongoClient(settings['MONGODB_HOST'],settings['MONGODB_PORT'])
    	db = conn[settings['MONGODB_DB']]
    	self.collection = db[settings['MONGODB_COLLECTION']]

    def get_released(self,released_str):
    	""" For some movies date information is absent.Dummy values are used for missing days and months"""
    	released_list = released_str.split()

    	#in case day info is missing:
    	if len(released_list) == 2:
    		released_str = "1 " + released_str

    	#both day and month are absent
    	elif len(released_list) == 1:
    		released_str = "1 January" + released_str
    		return str(released_str)
    	#return datetime.strptime(str(released_str),"%d %B %Y")

    def process_item(self,item,spider):
    	"""This function is responsible for storing the movie items in the collection.We do not allow duplicates.That is ensured by the movie_id identifier,which
    	   is uniquely assigned to movies by imdb"""
    	item_dict = dict(item)
    	
    	# before an insertion takes place we check if the movie already exists

    	if self.collection.find({"movie_id": item_dict["movie_id"]}).count() > 0:
    		return item

    	#item_dict['released'] = self.get_released(item_dict['released'])
    	item_dict['released'] = str(item_dict['released'])	
    	item_dict['produced'] = str(item_dict['produced'])	
    	# time of insertion
    	item_dict['inserted'] = datetime.now()
    	self.collection.insert(item_dict)

    	return item