# First Main File
import streamlit
import pandas
import requests
streamlit.title('......Dinner Time')
streamlit.header('Menu')
streamlit.text('🥣  Dosey')
streamlit.text('🥗 Uppittu')
streamlit.text('🥑🍞 Avocado Toast')

# Load the Fruit List
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit') 
#streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado' ,'Peach' ,'Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
#streamlit.dataframe(my_fruit_list)
streamlit.dataframe(fruits_to_show)

streamlit.header("Fruityvice Fruit Advice!")
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())


                
                 
