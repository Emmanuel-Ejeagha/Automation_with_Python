import streamlit as st
import pandas as pd


data = {
  'Series_1':[1, 3, 4, 5, 7, 6],
  'Series 2':[10, 30, 40, 100, 200, 13]
}

app = pd.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Testing Streamlit with Python')
st.write('''This is our first Web App.
         Enjoy it!''')
st.write(app)
st.line_chart(app)
st.area_chart(app)

myslider = st.slider('Celsius')
st.write(myslider, 'in Fahrenheit is', myslider * 9/5 + 32)