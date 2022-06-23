import streamlit as st
import pandas


data ={
    'series1': [1,3,4,5,7],
    'series2': [10,30,40,60,70]
}

df=pandas.DataFrame(data)

st.title('Our First Streamlit App')
st.subheader('Introducing Streamlit inAutomate Everyting with Python')
st.write("""
    This is our first web app.
    Enyoyed it!
""")

st.write(df)
st.line_chart(df)
st.area_chart(df)

myslider =st.slider("Celcius")
st.write(myslider, 'in Fahrenheit is', myslider *9/5 +32)
