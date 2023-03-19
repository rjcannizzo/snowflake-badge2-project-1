import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

def get_fruityvice_data(choice: str):
    fruityvice_response = requests.get(f"{BASE_URL}{choice}")       
    return pandas.json_normalize(fruityvice_response.json())  

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

streamlit.header('Fruityvice Fruit Advice')
BASE_URL = "https://fruityvice.com/api/fruit/"
try:
    choice = streamlit.text_input('What fruit would you like information about?')
    if not choice:
        streamlit.error("Please select a fruit to get information.")    
    else:
        fruityvice_normalized = get_fruityvice_data(choice)       
        streamlit.dataframe(fruityvice_normalized)
except URLError as e:
    streamlit.error()

streamlit.text("The fruit load list contains:")

def get_fruit_load_list():
    with my_cnx.cursor() as cur:
        cur.execute("select * from fruit_load_list")
        return cur.fetchall()        

if streamlit.button("Get Fuit Load List"):    
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    fruit_data = get_fruit_load_list()
    streamlit.dataframe(fruit_data)
    my_cnx.close()
    

def insert_row_snowflake(fruit: str):
    query = "insert into fruit_load_list values ({})".format(fruit)
    with my_cnx.cursor() as cur:
        cur.execute(query)
        return "Thanks for adding " + fruit


new_fuit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button("Get Fuit Load List"):    
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    msg = insert_row_snowflake(new_fuit)
    streamlit.text(msg)
    my_cnx.close()

streamlit.stop()