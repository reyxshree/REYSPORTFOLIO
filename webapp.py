import pandas as pd
import streamlit as st
import plotly.express as px
from PIL import Image

st.set_page_config(page_title='Attendance Managment System')
st.header('ATTENDANCE MANAGEMENT SYSTEM')
st.subheader('ATTENDANCE')

### --- LOAD DATAFRAME
excel_file = 'Final output.xlsx'
sheet_name = 'Final output'

df = pd.read_excel(excel_file,
                    sheet_name=sheet_name,
                     usecols='A:H',
                     header=0)

st.dataframe(df)   

pie_chart = px.pie(df,
               title='Attendance Chart',
               values='Total',
               names='Name')
          
st.plotly_chart(pie_chart)

image =Image.open('images/survey.jpg')
st.image(image,
        caption='Designed by slidesgo / Freepik',
        use_column_width=True)