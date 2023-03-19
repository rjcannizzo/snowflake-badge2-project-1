import streamlit
import pandas
import requests
import snowflake.connector

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avacado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado'])
fruits_to_show = my_fruit_list.loc[selected]
streamlit.dataframe(fruits_to_show)

import requests

streamlit.header('Fruityvice Fruit Advice')

choice = streamlit.text_input('What fruit would you like information about?', "Kiwi")
BASE_URL = "https://fruityvice.com/api/fruit/"

fruityvice_response = requests.get(f"{BASE_URL}{choice}")
# creates a Pandas dataframe by flattening a json object
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# displays a Pandas dataframe 
streamlit.dataframe(fruityvice_normalized)
