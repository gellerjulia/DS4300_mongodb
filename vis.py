# visualizations.py
import matplotlib.pyplot as plt
import seaborn as sns
import math
from collections import Counter
import plotly.express as px
import pandas as pd
from wordcloud import WordCloud

class Visualizations: 
    def bar_chart(data, x_label, y_label, title):
        x_values = [entry['_id'] for entry in data]
        y_values = [entry['count'] for entry in data]

        plt.bar(x_values, y_values)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.title(title)
        plt.xticks(rotation=15, ha='right')
        plt.show()
        
    def vis_ratings(data):
        ratings = [entry['stars'] for entry in data]
        counts = Counter(ratings)
        plt.bar(list(counts.keys()), list(counts.values()))
        plt.xlabel('Stars')
        plt.ylabel('Number of Restaurants')
        plt.title('Restaurants with 4+ Stars')
        plt.show()
        
    def vis_bubble(data):
        cities = [entry['_id'] for entry in data[:50]]
        counts = [entry['count'] for entry in data[:50]]
        plt.scatter(cities, counts, s=counts, alpha=0.5)
        plt.xlabel('City')
        plt.ylabel('Number of Businesses')
        plt.title('Top Cities with the most businesses')
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def vis_wordcloud(data):
    
       # Generate the word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies({entry['_id']: entry['count'] for entry in data})

        # Display the word cloud using matplotlib
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud of Business Types')
        plt.show()

        
            
        
    def vis_food_types(data, city):
        # Extract Food types from the data
        types = [entry['Food type'] for entry in data if 'Food type' in entry]

        # Count occurrences of each Food type
        counts = Counter(types)

        # Select top categories and group the rest
        top_categories = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)[:15])
        other_count = sum(counts.values()) - sum(top_categories.values())
        top_categories['Other'] = other_count

        # Plotting
        plt.pie(top_categories.values(), labels=top_categories.keys(), autopct='%1.1f%%', startangle=140)
        plt.axis('equal')
        plt.title(f'Top Restaurant Categories in {city}')
        plt.show()

    def vis_kid_friendly_businesses(result, city):
        # Extract the first category from each business
        categories = [entry.get('categories', [])[0] if len(entry.get('categories', [])) > 1 else 'N/A' for entry in result]


        # Count occurrences of each category
        counts = Counter(categories)
        
        # Select top categories and group the rest
        top = dict(sorted(counts.items(), key= lambda item: item[1], reverse=True) [:50])
        other_count = sum(counts.values()) - sum(top.values())
        top["Other"] = other_count

        # Plotting
        plt.bar(top.keys(), top.values())
        plt.xlabel('Business Categories')
        plt.ylabel('Number of Businesses')
        plt.title(f'Top Kid-Friendly Businesses in {city}')
        plt.xticks(rotation=45, ha='right')
        plt.show()

