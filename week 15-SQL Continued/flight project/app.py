import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px

db = DB()
st.sidebar.title('Flights Analystic')

user_option= st.sidebar.selectbox(label='menu',options=['Select one','Check flights','Analytics'])

if user_option == 'Check flights':
    st.title('Check Flights')
    
    col1,col2 = st.columns(2)
    
    with col1:
        cities_names = db.fetch_city_names()
        source = st.selectbox(label='Source',options= sorted(cities_names))
        
    with col2:
        cities_names = db.fetch_city_names()
        destination = st.selectbox(label='Destination',options= sorted(cities_names))
        
    if st.button('Search'):
        results = db.fetch_all_flights(source,destination)
        st.dataframe(results)
        
elif user_option == 'Analytics':
    st.title('Analytics')
    
    airline ,frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Airline Bar graph")
    st.plotly_chart(fig ,theme="streamlit",)
    
    city,frequency1 = db.busy_airport()
    fig = px.bar(
        x= city,
        y = frequency1,
        labels= {
            'x': 'city',
            'y': 'count'
        }
    )

    st.plotly_chart(fig, theme="streamlit",)


    date, frequency2 = db.daily_frequency()

    print(len(date))
    print(len(frequency2))
    fig = px.line(
        x=date,
        y=frequency2
    )

    st.plotly_chart(fig, theme="streamlit", use_container_width=True)

else:
    st.title('Tell about the project')
    