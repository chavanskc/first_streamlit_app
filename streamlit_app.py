# First Main File
import streamlit
import pandas
streamlit.title('......Dinner Time')
streamlit.header('Menu')
streamlit.text('🥣  Dosey')
streamlit.text('🥗 Uppittu')
streamlit.text('🥑🍞 Avocado Toast')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

                
                 
