import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px

df = pd.read_csv(filepath_or_buffer=r'C:\Users\sumit\My_code_files\Week 9 -Data Visulziation\plotly project\india.csv')

# selection of state 
list_of_states = list(df['State'].unique())
list_of_states.insert(0,'Overall india')

# selection of primary and secondary parameter 
primary_list = df.columns[4:].to_list()
secondary_list = df.columns[4:].to_list()

st.sidebar.title('India ka Data Viz')

# sidebar selectbox
selected_state = st.sidebar.selectbox(label='Select a State',options=list_of_states)

primary = st.sidebar.selectbox(label='Select Primary Parameter ',options=primary_list)
secondary = st.sidebar.selectbox(label='Select secondary Parameter ',options=secondary_list)

# user press a button and we plot the graph
plot = st.sidebar.button('Plot Graph')

# make two cases for overall india and state
if plot:
    st.text('Size represent primary parameter')
    st.text('Color represents secondary parameter')
    if selected_state == 'Overall India':
        # plot for india
        fig = px.scatter_map(data_frame=df,lat="Latitude", lon="Longitude",size=primary, color=secondary ,zoom=6, size_max=35,
                            color_continuous_scale=px.colors.cyclical.IceFire, width=1200, height=600,hover_name='District')

        st.plotly_chart(fig,use_container_width=True)
    else:
        # plot for state
        state_df = df[df['State'] == selected_state]

        fig = px.scatter_map(data_frame=state_df,lat="Latitude", lon="Longitude",size=primary, color=secondary ,zoom=6, size_max=35,
                            color_continuous_scale=px.colors.cyclical.IceFire, width=1200, height=600,hover_name='District')

        st.plotly_chart(fig, use_container_width=True)