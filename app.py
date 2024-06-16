import streamlit as st
import pandas as pd
import plotly_express as px

car_data = pd.read_csv('/Users/eric/Desktop/My Projects/my_project/Sprint5_Project/vehicles.csv')
hist_button = st.button('Create Histogram')

if hist_button:
    st.write('We Create a Histogram for our DataFrame')
fig = px.histogram(car_data, x = 'odometer')
st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button('Create Scatter')
if scatter_button:
    st.write('We Created a Scatter Chart')   
fig = px.scatter(car_data, x='odometer', y='price', title='Odometer vs Price')
st.plotly_chart(fig, use_container_width=True)



show_hist = st.checkbox('Show Histogram')
show_scatter = st.checkbox('Show Scatter')

if show_hist:
    st.write('We Create a Histogram for our DataFrame')
if show_scatter:
    st.write('We Created a Scatter Chart')