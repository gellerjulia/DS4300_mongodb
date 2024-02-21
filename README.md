# Yelp Dataset Exploration

This Python script allows you to explore the Yelp Academic Dataset using MongoDB queries and visualize the data with various charts.

## Prerequisites

- Python 3.x
- MongoDB
- Required Python packages (pymongo, matplotlib, json, wordcloud, collections)

## Setup

1. Install Python and MongoDB on your machine.
2. Clone or download this repository.
3. Import the Yelp Academic Dataset into your MongoDB database.
4. Update the script with your MongoDB database and collection information.

## Usage

1. Run the script `main.py`.
2. Follow the directions in the terminal, and choose a question number to explore from the given options.
3. Follow the prompts, such as entering a city or confirming to explore another question.
4. For visualizations, drag the window to enlarge if needed.
5. Close the visualization window to return to the main menu. The code will ask you if you wish to explore another question. If yes, repeat the above operations.

## Questions Explored

1. High level snapshot of the data
2. Find restaurants with 4+ star rating
3. Find restaurants with takeout
4. Find businesses that are good for kids

## Notes
- This dataset is containing mostly data from the state Arizona.  
- Ensure that the entered city is included in the dataset.
- Enlarge the visualization window to view all x-labels in charts.
- Close the visualization window to explore another question.

## Author And Contributions

Ceara Zhang - Ceara contributed by creating the API by coding the query functions in python and outputting various visualizations for different prompts to showcase the queried data. 

Julia Geller - Julia contributed by choosing the dataset, declaring questions to explore the data with, and creating and documenting the Mongo queries and output results.