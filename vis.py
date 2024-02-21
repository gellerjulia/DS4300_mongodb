"""
Julia Geller and Ceara Zhang
DS4300 / HW3 Mongo Database
Created 17 Feb 2024
Updated: 20 Feb 2024

Visualizations.py:

"""
import matplotlib.pyplot as plt
from collections import Counter
from wordcloud import WordCloud

class Visualizations: 
    @staticmethod
    def plot_bar(x, y, xlabel, ylabel, title, rotation='horizontal', color='skyblue'):
        plt.bar(x, y, color=color)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.xticks(rotation=rotation)
        plt.show()
    
    def vis_bus_per_state(data): 
        """Bar chart showing number of businesses per state"""
        states = [entry['_id'] for entry in data]
        counts = [entry['count'] for entry in data]
        Visualizations.plot_bar(states, counts, 'State', 'Number of Businesses per State', 'Number of Businesses per State')
        
    def vis_ratings(data):
        """Bar chart showing 4+ rating restaurants"""
        ratings = [entry['stars'] for entry in data]
        counts = Counter(ratings)
        
        # Plotting
        Visualizations.plot_bar(counts.keys(), list(counts.values()), 'Stars', 'Number of Restaurants', 'Restaurants with 4+ Stars')
        
    def vis_bubble(data):
        """Bubble chart showing cities with most businesses"""
        cities = [entry['_id'] for entry in data[:50]]
        counts = [entry['count'] for entry in data[:50]]
        plt.scatter(cities, counts, s=counts, alpha=0.5)
        plt.xlabel('City')
        plt.ylabel('Number of Businesses')
        plt.title('Top Cities with the most businesses')
        plt.xticks(rotation=45, ha='right')
        plt.show()

    def vis_wordcloud(data):
        """Wordcloud showing business types"""
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies({entry['_id']: entry['count'] for entry in data})

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.title(f'Word Cloud of Business Types')
        plt.show()
        
    def vis_food_types(data, city):
        """Pie chart showing top food categories for a city"""
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
        """Bar chart showing most popular types of places that are kid friendly"""
        # Extract the first category from each business
        categories = [entry.get('categories', [])[0] if len(entry.get('categories', [])) > 1 else 'N/A' for entry in result]

        # Count occurrences of each category
        counts = Counter(categories)
        
        # Select top categories and group the rest
        top = dict(sorted(counts.items(), key= lambda item: item[1], reverse=True) [:40])
        other_count = sum(counts.values()) - sum(top.values())
        top["Other"] = other_count
        
        # Plotting
        Visualizations.plot_bar(top.keys(), top.values(), 'Business Categories', 'Number of Businesses', f'Top Kid-Friendly Businesses in {city}', rotation=45)

