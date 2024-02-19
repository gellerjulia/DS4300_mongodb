# visualizations.py
import matplotlib.pyplot as plt
import math

def bar_chart(data, x_label, y_label, title):
    x_values = [entry['_id'] for entry in data]
    y_values = [entry['count'] for entry in data]

    plt.bar(x_values, y_values)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.xticks(rotation=15, ha='right')
    plt.show()
