# main_script.py
from mongo_api import MongoAPI
from vis import bar_chart

if __name__ == "__main__":
    # Initialize MongoDB API
    api = MongoAPI(db_name='your_database_name', collection_name='biz')

    # Example usage
    print("Businesses per state:")
    state_data = api.businesses_per_state()
    print(state_data)

    # Visualize data
    bar_chart(state_data, x_label='State', y_label='Number of Businesses', title='Businesses per State')

    print("\nDifferent types of businesses:")
    print(api.get_business_types())

    print("\nPhoenix businesses offering takeout:")
    phoenix_takeout_data = api.businesses_with_takeout()
    print(phoenix_takeout_data)

    # Add more calls to test other API functions...
