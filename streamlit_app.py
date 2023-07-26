# First Main File
import streamlit
import pandas
import requests
import snowflake.connector
from  urllib.error import URLError

def get_fruityvice_data(this_fruit_choice):
  #streamlit.write('The user entered ', fruit_choice)
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
  #streamlit.text(fruityvice_response.json())
  # write your own comment -what does the next line do? - convert JSON into table/frame
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  # write your own comment - what does this do? Show as table (Data Frame)
  return fruityvice_normalized
  
def get_fruit_load_list():
  my_cur = my_cnx.cursor()
  #my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
  my_cur.execute("SELECT * from fruit_load_list")
  my_data_row = my_cur.fetchall()
  return my_data_row

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error('Please select a fruit')
  else:
    streamlit.dataframe(get_fruityvice_data(fruit_choice))
    
    
except URLError as e:
  streamlit.error()

#streamlit.stop()


streamlit.text("Hello from Snowflake:")
# display as text.. as it is
#streamlit.text(my_data_row)
# display as DataFrame
if streamlit.button('Load Fruit List'):
  
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  my_data_rows = get_fruit_load_list()
  streamlit.dataframe( my_data_rows)
                    
#streamlit.dataframe(my_data_row)

add_fruit = streamlit.text_input('Add a Fruit')
streamlit.text(add_fruit)
query_insert = "insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('{fruit_entered}')"
query_insert = query_insert.format(fruit_entered = add_fruit)
my_cur.execute(query_insert)



                
                 
