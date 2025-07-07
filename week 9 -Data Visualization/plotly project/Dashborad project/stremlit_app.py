import pandas as pd
import streamlit as st


########################################
# Setup
########################################

st.set_page_config(
    page_title='Complaning Dashbord',
    page_icon='📈'
)

########################################
# load data 
########################################
st.title("📞What are the usual failing products?")

@st.cache_data(max_entries=5)
def load_data(path: str):
    data = pd.read_csv(path,parse_dates=['Date Sumbited',"Date Received"])
    return data

df = load_data(path='./data/Financial Consumer Complaints.csv')
all_products = df['Product'].unique()


########################################
# UI 
########################################



selected_product = st.selectbox(label='All Products',options=all_products)#options=None)

st.title(selected_product)

# row_metrics = st.columns(2)
row_left,row_right = st.columns(2)

#st.write(type(row_metrics))

row_left.metric('left metric',15)
row_right.metric('right matric', 15)
with  st.container(border=True):
    st.metric('count', 42)


st.dataframe(df,hide_index=True)

