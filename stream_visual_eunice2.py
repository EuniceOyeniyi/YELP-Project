import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import re
import plotly.express as px
from PIL import Image

df = pd.read_csv("Resturantdata.csv")
df_pub = pd.read_csv("Pubdata.csv")
df_hotel = pd.read_csv("Hoteldata.csv")

# df_test = pd.read_csv("C:/Users/andre/Desktop/Resturantdata.csv")

plt.rcdefaults()
plt.rcParams.update({'axes.facecolor':'black'})
# plt.figure(facecolor='black') 

data_select = st.sidebar.selectbox("Select the data you want to see", ("Home", "Restaurants", "Hotels", "Pubs"))

#   Homepage
if data_select == "Home":

    st.title('Accommodation, Restaurants & Drink Services in Berlin')
    st.header('Why accommodation, food, and drink services industry?')
    st.markdown("""The accommodation industry and the food and drink services industry have faced unprecedented change due to the coronavirus (COVID-19) pandemic.
    Up until this moment, the accommodation, food, and drink services industry have been seeing consistent year-over-year growth in all its sectors.
    Yet, while the pandemic has proved to be a difficult time for these industries, it is still predicted to see growth.""")


    st.header('Team member')
    st.markdown('* *Andrea*')
    st.markdown('* *Eunice*')

    # px.set_mapbox_access_token(open(".mapbox_token").read())
    # fig = px.scatter_mapbox(df_test, lat="Latitude", lon="Longitude",zoom=12, size = 'reviews', color='rating', 
    # width=900, height=600, opacity=1, template="plotly_dark")
    # st.plotly_chart(fig) 

#   Restaurants
elif data_select == "Restaurants":

    st.title("Restaurant insights")
    
    #   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df['Neighbourhoods'].value_counts(), height=600, width=800, labels={
        "value": "Number of restaurants per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)
    
    st.text('Little description here')

    #   Graph n.2
    
    fig = px.bar(df['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
            "value": "Number of Restaurants with respective price range",
            "index": "Price range (in euros)"
    },
    title='Price range of restaurants in Berlin')
    st.write(fig)    
    
    #   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df["Type_of_resturant"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of restaurants",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')

    #   Graph n.4 
    
    st.subheader('Need to do it faincier')

    st.set_option('deprecation.showPyplotGlobalUse', False)
    plt.figure(facecolor='red') 
    df[['Ratings','Prices']].groupby(['Prices']).value_counts().plot(kind='bar',color='royalblue')
    plt.gca().get_xticklabels()[0].set_color('white')
    plt.gca().get_xticklabels()[1].set_color('white')
    plt.gca().get_xticklabels()[2].set_color('white')
    plt.gca().get_xticklabels()[3].set_color('white')
    plt.gca().get_xticklabels()[4].set_color('white')
    plt.gca().get_xticklabels()[5].set_color('white')
    plt.gca().get_xticklabels()[6].set_color('white')
    plt.gca().get_xticklabels()[7].set_color('white')
    plt.gca().get_xticklabels()[8].set_color('white')
    plt.gca().get_xticklabels()[9].set_color('white')
    plt.gca().get_xticklabels()[10].set_color('white')
    plt.gca().get_xticklabels()[11].set_color('white')
    plt.gca().get_xticklabels()[12].set_color('white')
    plt.gca().get_xticklabels()[13].set_color('white')
    plt.gca().get_xticklabels()[14].set_color('white')
    plt.gca().get_yticklabels()[0].set_color('white')
    plt.gca().get_yticklabels()[1].set_color('white')
    plt.gca().get_yticklabels()[2].set_color('white')
    plt.gca().get_yticklabels()[3].set_color('white')
    plt.gca().get_yticklabels()[4].set_color('white')
    plt.gca().get_yticklabels()[5].set_color('white')
    plt.gca().get_yticklabels()[6].set_color('white')
    plt.xlabel('Prices, Ratings',color='white')
    plt.ylabel('Counts',color='white')
    plt.title('Most prefered price range',color='white')
    st.pyplot()

    #   Fancier but..
    df_prices = df[['Ratings','Prices']].groupby(['Prices']).value_counts()
    test = px.bar(df_prices, x=df_prices.index.get_level_values(1),y=0)
    st.write(test)
    st.text('Little description here')

    #   Graph n.5

    st.subheader('Need to do it faincier')
    df[['Type_of_resturant','Ratings']].groupby('Type_of_resturant').value_counts().nlargest(10). plot(kind='barh')

    plt.xlabel('Counts')
    plt.title('Most prefered type of restaurant by rating')
    st.pyplot()
    st.text('Little description here')

    plt.figure(facecolor='black') 
    df['Neighbourhoods'].value_counts().nlargest(10).plot(kind = 'pie',figsize=(8,8), autopct = '%1.1f%%',textprops={'color':"w"})
    
    plt.title('Cluster location of hotels',color='white')
    st.pyplot()

#   Hotels

elif data_select == "Hotels":

    st.title("Hotels insights")


#   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df_hotel['Neighbourhoods'].value_counts(), orientation='h', height=700, width=850, labels={
        "value": "Number of hotels per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)

    st.text('Little description here')


#   Graph n.2

    fig = px.bar(df_hotel['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of hotels with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of hotels in Berlin')
    st.write(fig)   

    st.text('Little description here')


#   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df_hotel["Type_of_hotels"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of hotels",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')




#   Pubs

elif data_select == "Pubs":

    st.title("Pubs insights")


#   Graph n.1

    st.subheader('Graph Title - to do')
    fig=px.bar(df_pub['Neighbourhoods'].value_counts(), orientation='h', height=700, width=850, labels={
        "value": "Number of pubs per neighbourhood",
        "index": "Neighbourhoods"
    })
    st.write(fig)

    st.text('Little description here')


#   Graph n.2

    fig = px.bar(df_pub['Prices'].value_counts(ascending=True), orientation='h', height=650, width=850, labels={
        "value": "Number of pubs with respective price range",
        "index": "Price range (in euros)"
    },
    title='Price range of pubs in Berlin')
    st.write(fig)   

    st.text('Little description here')


#   Graph n.3

    st.subheader('Graph Title - to do')
    df_type = px.bar(df_pub["Type_of_pubs"].value_counts(ascending=True).nlargest(10), height=600, width=800, labels={
        "value": "Type of pubs",
        "index": "Categories"
    })
    st.write(df_type)
    st.text('Little description here')













