# First Main File
import streamlit
import pandas
import requests
import snowflake.connector
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

fruit_choice = streamlit.text_input('What fruit would you like information about?','Kiwi')
streamlit.write('The user entered ', fruit_choice)
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
#streamlit.text(fruityvice_response.json())
# write your own comment -what does the next line do? - convert JSON into table/frame
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do? Show as table (Data Frame)
streamlit.dataframe(fruityvice_normalized)

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_cur.execute("SELECT * from fruit_load_list")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
# display as text.. as it is
#streamlit.text(my_data_row)
# display as DataFrame
streamlit.dataframe(my_data_row)


                
                 
