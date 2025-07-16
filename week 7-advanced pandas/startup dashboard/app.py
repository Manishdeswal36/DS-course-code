import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 

st.set_page_config(layout = 'wide',page_title='StartUp Analysis')

st.sidebar.title('Startup Funding Analysis')
df = pd.read_csv('startup_clean.csv')
df['date'] = pd.to_datetime(df['date'],errors='coerce')
# make a new month coloumn and yer coloum
df['month'] = df['date'].dt.month
df['year'] = df['date'].dt.year

def load_overall_details():
    # total investment money
    total = round(df['amount'].sum())
    # max amount invested in a startup
    max_funding = df.groupby('startup')['amount'].max().sort_values(ascending=False).values[0]
    # avg fundging  invested in a startup
    avg_funding = round(df.groupby('startup')['amount'].sum().mean())
    # total  number of funded startup
    total_startup = df['startup'].nunique()
    
    col1,col2,col3,col4 = st.columns(4)
    col1.metric(label='Total',value=f'{total} Cr.',)
    col2.metric(label='Maximum funding',value=f'{max_funding} Cr.' )
    col3.metric(label='Avg funding',value=f'{avg_funding} Cr.' )
    col4.metric(label='funded startups',value=f'{total_startup} ' )
    
    # month by month analysis 
    st.header('Month and Month graph')
    selected_option = st.selectbox('Select Type',['Total','Count'])
    if selected_option == 'Total':
        temp_df = df.groupby(['year', 'month'])['amount'].sum().reset_index()
    else:
        temp_df = df.groupby(['year', 'month'])['amount'].count().reset_index()

    temp_df['x_axis'] = temp_df['month'].astype('str') + '-' + temp_df['year'].astype('str')

    fig3, ax3 = plt.subplots()
    ax3.plot(temp_df['x_axis'], temp_df['amount'])
    # Reduce the number of x-axis labels (show every nth label)
    n = max(1, len(temp_df) // 10)  # Adjust this to control label density
    ax3.set_xticks(temp_df['x_axis'][::n])  # Show every nth label

    # Reduce font size
    ax3.set_xticklabels(temp_df['x_axis'][::n], fontsize=8)  # Adjust font size as needed

    # Rotate labels slightly (if needed) to prevent overlap
    plt.xticks(rotation=20, ha='right')

    st.pyplot(fig3)



def load_investor_details(investor):
    st.title(investor)
    # load the recent 5 investments of the investors
    last5_df = df[df['investers'].str.contains(investor)].head()[['date','startup','vertical','city','round','amount']]
    st.subheader('Most Recent Investments')
    st.dataframe(last5_df)
    
    col1,col2 = st.columns(2)
    with col1:
        # biggest inventest 
        big_series = df[df['investers'].str.contains(investor)].groupby('startup')['amount'].sum().sort_values(ascending=False).head()
        st.subheader('Biggest  Investments ')
        #st.dataframe(big_series)
        fig ,ax  = plt.subplots()
        ax.bar(big_series.index,big_series.values)
        
        st.pyplot(fig)
        
    with col2:
        # investvemtns in each sector 
        vertical_series = df[df['investers'].str.contains(investor)].groupby('vertical')['amount'].sum().sort_values(ascending=False)
        st.subheader('Sector Investment')
        # polt the pie chart
        fig1 ,ax1  = plt.subplots()
        ax1.pie(x=vertical_series.values,labels=vertical_series.index,autopct='%0.01f%%')
        
        st.pyplot(fig1)
    
    # year wise investemnt line chart
    st.subheader('Year wise Investment')
    # plot the line chart
    
    year_series = df[df['investers'].str.contains(investor)].groupby('year')['amount'].sum()
    fig2 ,ax2  = plt.subplots()
    ax2.plot(year_series.index ,year_series.values)
    st.pyplot(fig2)

option = st.sidebar.selectbox('Select One',['Overall Analysis','StartUp','Investor'])

if option =='Overall Analysis':
    st.title('Overall Analysis')
    button_0 = st.sidebar.button('Show overall analysis')
    if button_0:
        load_overall_details()
elif option == 'StartUp':
    st.sidebar.selectbox('Select Startup' ,sorted(df['startup'].unique().tolist()))
    st.title('StartUp')
    button_1 = st.sidebar.button('Find Startup details')
elif option == 'Investor':
    selected_invesor = st.sidebar.selectbox('Select Investor' ,sorted(set(df['investers'].str.split(',').sum())))
    st.title('Investor')
    button_2 = st.sidebar.button('Find Investor details')
    if button_2:
        load_investor_details(selected_invesor)


