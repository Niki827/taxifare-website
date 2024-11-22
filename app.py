import streamlit as st
import datetime
import requests

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''
# date and time input
d = st.date_input('Enter date for taxi ride', datetime.date(2014,7,6))
st.write('date for taxi ride:', d)

t = st.time_input('Enter time for taxi ride', datetime.time(19, 18))
st.write('time for taxi ride:', t)

# longitudes and latitudes
pickup_longitude = st.number_input('Insert a pickup longitude', -73.950655)
st.write('the current pickup longitude is:', pickup_longitude)

pickup_latitude = st.number_input('Insert a pickup latitude', 40.783282)
st.write('the current pickup latitude is:', pickup_latitude)

dropoff_longitude = st.number_input('Insert a dropoff longitude', -73.984365)
st.write('the current dropoff longitude is:', dropoff_longitude)

dropoff_latitude = st.number_input('Insert a dropoff latitude', 40.769802)
st.write('the current dropoff latitude is:', dropoff_latitude)


passenger_count = st.slider('Select a passenger count', 1, 10, 3)
st.write('the current passenger count is:', passenger_count)





'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''

# building the params dict
params = {'pickup_datetime' : f'{d} {t}',
          'pickup_longitude': pickup_longitude,
          'pickup_latitude': pickup_latitude,
          'dropoff_longitude': dropoff_longitude,
          'dropoff_latitude': dropoff_latitude,
          'passenger_count': passenger_count}

# call the api
response = requests.get(url=url, params=params).json()

with st.echo():
    st.write(f"Fare prediction: ${round(response['fare'], 2)}")
