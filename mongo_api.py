"""
Julia Geller and Ceara Zhang
DS4300 / HW3 Mongo Database
Created 17 Feb 2024
Updated: 20 Feb 2024

mongo_api.py:
"""
from pymongo import MongoClient

class MongoAPI:
    def __init__(self, db_name, collection_name):
        """
        Initialize MongoDB API instance.

        :param db_name: Name of the MongoDB database.
        :param collection_name: name of the MongoDB collection
        """
        self.client = MongoClient('localhost', 27017)
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def import_data(self, data):
        """
        Imports the data into the current database and collection.

        params:
        data: list of dict data
        """
        self.collection.insert_many(data)
        
    def destroy_db(self, db):
        """
        Destroys the given database.

        params:
        db: str name of database
        """
        self.client.drop_database(db)

    def businesses_per_state(self):
        """
        Q1: Get the number of businesses per state,
        sorted in descending order.

        :return: List of dictionaries containing state and business count.
        """
        pipeline = [
            {"$group": {"_id": "$state", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        return list(self.collection.aggregate(pipeline))

    def get_business_types(self):
        """
        Q2: Get a list of all different types of businesses with their count.

        return: List of dictionaries containing business type and count.
        """
        pipeline = [
            {"$unwind": "$categories"},
            {"$group": {"_id": "$categories", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result


    def num_businesses_per_city(self):
        """
        Q3: Get the number of businesses per city
        :param state:
        :return:
        """
        pipeline = [
            {"$group": {"_id": "$city", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}}
        ]
        result = list(self.collection.aggregate(pipeline))
        return result

    def businesses_with_takeout(self, city):
        """
        Q6: Get businesses of a city offering takeout, returning name and full address.

        :return: List of dictionaries containing name and full address of businesses.
        """
        query = {"city": city, "attributes.Take-out": True}
        projection = {"name": 1, "categories": 1, "full_address": 1}
        result = list(self.collection.find(query, projection))
    
        for business in result:
            # get the first non "food" or "Restaurants" cateogry tag
            cat = business.get("categories", [])
            first_non_food_category = next((cat for cat in cat if cat.lower() not in {'food', 'restaurant'}), None)
            business['Food type'] = first_non_food_category
            business.pop("categories", None)
            
        return result
                    

    def high_business_rating(self, city):
        """
        Get restaurants with 4+ rating in a city using aggregation pipeline.

        :param city: The city to filter by.
        :return: A tuple containing a list of restaurants and the total count.
        """

        result = [
            {"$match": {"city": city, "stars": {"$gte": 4.0, "$mod": [0.25, 0]}, "categories": "Restaurants"}},
            {"$group": {"_id": None, "count": {"$sum": 1}}},
        ]

        # Projection to include only specified fields
        projection = {"_id": 0, "city": 1, "stars": 1, "name": 1, "full_address": 1}
        restaurants = list(self.collection.find({"city": city, "stars": {"$gte": 4.0}}, projection))
        return restaurants


    def businesses_kids(self, city):
        """
        Get businesses that are good with kids
        
        :param city: the city to filter by
        """
        query = {"city": city, "attributes.Good for Kids": True}
        projection = {"name": 1, "full_address": 1, "categories": 1}
        result = list(self.collection.find(query, projection))
        return result
    
    def get_all_cities(self):
        """
        Get a list of all uniquer cities in the dataset
        
        """
        query = {}
        projection = {"city": 1, "_id": 0}
        result = list(self.collection.find(query, projection))
        cities = list(set(entry['city'] for entry in result if 'city' in entry))
        return cities
        