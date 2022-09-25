#! ./venv/Scripts/python

# INF601 - Advanced Programming in Python
# Krushil Naik
# Mini Project 2

# (5/5 points) Initial comments with your name, class and project at the top of your .py file.
# (20/20 points) Using a data source of your choice, such as data from data.gov or using the Faker package, generate or retrieve some data for creating basic statistics on. This will generally come in as json data, etc.
# Think of some question you would like to solve such as:
# "How many homes in the US have access to 100Mbps Internet or more?"
# "How many movies that Ridley Scott directed is on Netflix?" - https://www.kaggle.com/datasets/shivamb/netflix-shows
# Here are some other great datasets: https://www.kaggle.com/datasets
# (10/10 points) Store this information in Pandas dataframe. These should be 2D data as a dataframe, meaning the data is labeled tabular data.
# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

# (5/5 points) Proper import of packages used.
import os
import matplotlib.pyplot as plt
import pandas as pd
import requests


if not os.path.exists("./charts"):
    os.mkdir("./charts")

city = "Tokyo"

# I'm aware this is unsafe, but unsure how this would be graded without it
API_KEY = "P6nDiEWzEias+qnnrMReaw==hAaNKc72nVArU8DT"

# Gather air quality data from the cities in the cities list
response = requests.get(
    f"https://api.api-ninjas.com/v1/airquality?{city=}",
    headers={"X-Api-Key": API_KEY},
)
