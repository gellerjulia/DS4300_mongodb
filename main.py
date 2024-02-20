# main_script.py
from mongo_api import MongoAPI
from vis import bar_chart

import matplotlib.pyplot as plt

if __name__ == "__main__":
    # Initialize MongoDB API
    api = MongoAPI(db_name='DS4300', collection_name='Yelp Dataset')

    print("Hi there! Below are some options to explore the dataset.")

    # High Level Querying
    print("1. High level snapshot of the data")
    
    # Detailed querying2
    print("2. Find restaurants with 4+ star rating")
    print("3. Find restaurants with takeout")
    print("4. Find businesses that are good for kids")
    # print("5. Find businesses with free wifi")
    
    choice = input("To learn more about a question, please enter the question number: ")

    if choice == "1":
        # Get businesses per state
        state_data = api.businesses_per_state()
        bar_chart(state_data, x_label='State', y_label='Number of Businesses', title='Businesses per State')

        #G et Number of businnesses for each type
        print("Types of businesses:")
        business_types = api.get_business_types()
        print(business_types)

        # Number of businesses per city
        print("Number of businesses per state: ")
        # bus_per_city = 
    
    elif choice == "2":
        # 4+ rating restaurants
        city = input("Enter the city: ")
        rating = api.high_business_rating(city)
        print(rating)
        plt.bar(list(rating.keys(), list(rating.values())))
        plt.xlabel('Stars')
        plt.ylabel('Number of Restaurants')
        plt.title('Restaurants with 4+ Stars')
        plt.show()

    elif choice == "3":
        # Get businesses with takeout in a city
        city = input("Enter the city: ")
        api.businesses_with_takeout(city)

    elif choice == "4": 
        # Get businesses that are good with kids
        city = input("Enter the city: ")
        api.businesses_kids(city)
        

    else:
        print("Invalid choice. Please enter a number 1-4.")


# if __name__ == "__main__":
#     # Initialize MongoDB API
#     api = MongoAPI(db_name='DS4300', collection_name='Yelp Dataset')

#     # Example usage
#     print("Businesses per state:")
#     state_data = api.businesses_per_state()
#     print(state_data)

#     # Visualize data
#     bar_chart(state_data, x_label='State', y_label='Number of Businesses', title='Businesses per State')

#     print("\nDifferent types of businesses:")
#     print(api.get_business_types())

#     print("\nPhoenix businesses offering takeout:")
#     phoenix_takeout_data = api.businesses_with_takeout('Boston')
#     print(phoenix_takeout_data)

#     # Add more calls to test other API functions...
