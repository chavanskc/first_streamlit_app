# First Main File
import streamlit
import pandas
streamlit.title('......Dinner Time')
streamlit.header('Menu')
streamlit.text('🥣  Dosey')
streamlit.text('🥗 Uppittu')
streamlit.text('🥑🍞 Avocado Toast')

# Load the Fruit List
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index(('Fruit) )
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)


                
                 
