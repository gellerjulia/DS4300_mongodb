# main_script.py
from mongo_api import MongoAPI
from vis import Visualizations
import json
import pprint as pp
from collections import Counter

import matplotlib.pyplot as plt

def explore_another_question():
    return input("Do you want to explore another question? (yes/no): ").lower() == "yes"


if __name__ == "__main__":
    # Initialize MongoDB API
 
    api = MongoAPI(db_name='DS4300', collection_name='Yelp Dataset')
    # api = MongoAPI(db_name='yelp_db', collection_name='biz')

     # import the data
    yelp_data = []
    with open('data/yelp_academic_dataset_business.json', 'r') as json_file:
        # Iterate through each line in the file
        for line in json_file:
            # Load the JSON data from each line
            yelp_data.append(json.loads(line))
    
    # insert data into current database and collection
    api.import_data(yelp_data)

    print("Hi there! Below are some options to explore the dataset.")

    while True: 
        # Querying
        print("1. High level snapshot of the data")
        print("2. Find restaurants with 4+ star rating")
        print("3. Find restaurants with takeout")
        print("4. Find businesses that are good for kids")
        # print("5. Find businesses with free wifi")
    
        choice = input("To learn more about a question, please enter the question number: ")

        if choice == "1":
            # Get businesses per state
            state_data = api.businesses_per_state()

            #G et Number of businnesses for each type
            print("Types of businesses:")
            business_types = api.get_business_types()
            Visualizations.heatmap(business_types)            

            # Number of businesses per city
            print("Number of businesses per city: ")
            bus_per_city = api.num_businesses_per_city()
            Visualizations.vis_bubble(bus_per_city)
    
        elif choice == "2":
            # 4+ rating restaurants
            city = input("Enter the city: ")
            rating = api.high_business_rating(city)
            print(rating)
            ratings = [entry['stars'] for entry in rating]
            counts = Counter(ratings)
            plt.bar(list(counts.keys()), list(counts.values()))
            plt.xlabel('Stars')
            plt.ylabel('Number of Restaurants')
            plt.title('Restaurants with 4+ Stars')
            plt.show()

        elif choice == "3":
            # Get businesses with takeout in a city
            city = input("Enter the city: ")
            takeout = api.businesses_with_takeout(city)
            Visualizations.vis_food_types(takeout, city)
            
        elif choice == "4": 
            # Get businesses that are good with kids
            city = input("Enter the city: ")
            kids = api.businesses_kids(city)
            Visualizations.vis_kid_friendly_businesses(kids, city)
        

        else:
            print("Invalid choice. Please enter a number 1-4.")

        if not explore_another_question():
            break
        
    # destroy the database (for testing purposes)
    api.destroy_db("yelp_db")
