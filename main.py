# main_script.py
from mongo_api import MongoAPI
from vis import bar_chart
import json
import pprint as pp

if __name__ == "__main__":
    # Initialize MongoDB API
    api = MongoAPI(db_name='yelp_db', collection_name='biz')

    # import the data
    yelp_data = []
    with open('data/yelp_academic_dataset_business.json', 'r') as json_file:
        # Iterate through each line in the file
        for line in json_file:
            # Load the JSON data from each line
            yelp_data.append(json.loads(line))
    
    # insert data into current database and collection
    api.import_data(yelp_data)

    # Example usage
    print("Businesses per state:")
    state_data = api.businesses_per_state()
    pp.pprint(state_data)

    print("\nDifferent types of businesses:")
    pp.pprint(api.get_business_types())

    print("\nNumber of businsses per city in Arizona:")
    num_biz_az = api.num_businesses_per_city('AZ')
    pp.pprint(num_biz_az)

    print("\nPhoenix businesses offering takeout:")
    phoenix_takeout_data = api.businesses_with_takeout('Phoenix')
    pp.pprint(phoenix_takeout_data)

    # Visualize data
    bar_chart(state_data, x_label='State', y_label='Number of Businesses', title='Number of Businesses per State')
    bar_chart(num_biz_az, x_label='City', y_label='Number of Businesses', title='Number of Businesses per City in Arizona')

    # destroy the database (for testing purposes)
    api.destroy_db("yelp_db")