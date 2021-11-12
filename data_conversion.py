# Imports
import pandas as pd

# File path to csv data
file_path = "Resources/cities.csv"

# Read the csv file into a dataframe and convert it to html
data = pd.read_csv(file_path)
data = data.set_index('City_ID')
data_html = data.to_html()

# Export the dataframe to the resources folder
with open("data_converted.html", "w") as file:
    file.write(data_html)