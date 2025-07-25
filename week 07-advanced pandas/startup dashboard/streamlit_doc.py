import streamlit as st
import pandas as pd 
import time

st.title('Startup Dashbaord')
st.header('I am learning streamlit ')
st.subheader('I am very happy and love it ')

st.write('This is normal text')

st.markdown(''' 
### morning affirmation
1. focus and flow
2. happy and exicted 
3. love the process
            ''')

st.code('''
def some_func(input)
    return input**2
''')

st.latex('x^2 +y^2 + 2 = 0')

df = pd.DataFrame({
    'Name': ['manish','anand','ayush','piyush','aryaveer'],
    'marks': [80,90,85,80,89],
    'package': [10,20,30,40,50]
    
})
st.dataframe(df)

st.metric('Reveneue','Rs3lakh','10%')

st.json({
    'Name': ['manish','anand','ayush','piyush','aryaveer'],
    'marks': [80,90,85,80,89],
    'package': [10,20,30,40,50]
    
})

st.image(r"C:\Users\sumit\my_download photos\bhakt parad\bhagawad_geeta_cover.jpeg")

st.video(r"C:\Users\sumit\My_code_files\manim_code_files\Manim Crash Course\media\videos\first_animation\1080p60\simple_animation.mp4")

st.sidebar.title('sidebar ka title')

col1,col2 = st.columns(2)
with col1:
    st.image(r"C:\Users\sumit\my_download photos\bhakt parad\bhagawad_geeta_cover.jpeg")

with col2:
    st.image(r"C:\Users\sumit\my_download photos\bhakt parad\bhagawad_geeta_cover.jpeg")

st.error('login failed')

st.success('login success')

st.warning('login chal raha ha')
st.info('login ho gaya')

bar = st.progress(0)

# for i in range(0,101):
#     time.sleep(0.1)
#     bar.progress(i)

email = st.text_input('enter email')
number = st.number_input('enter age')
date = st.date_input('enter registration date')

import streamlit as st

email = st.text_input('enter email')
password = st.text_input('enter password')
gender = st.selectbox('select gender',['male','female','others'])

our_button = st.button('login karo')

# if buttion is clicked
if our_button:
    if email =='manishdeswal@gmail.com' and password == '1234':
        st.success('login sucesss')
        st.balloons()
        st.write(gender)
    else:
        st.error('login failured')
        
        
import streamlit as st
import pandas as pd
# user upload the csv file and
# apko uska upar kuch analysis karna ha  
# we do pandas describe func on it and display it 
file = st.file_uploader('upload the csv file')
if file is not None:
    df = pd.read_csv(file)
    st.dataframe( df.describe() )