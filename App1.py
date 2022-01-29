import streamlit as st
import pandas as pd
import csv
import pickle
import numpy as np
import datetime
import darts
import matplotlib.pyplot as plt

from darts import TimeSeries

data = pd.read_csv("final.csv")

model1 = pickle.load(open('finalized_model1.pkl', 'rb'))
model2 = pickle.load(open('finalized_model2.pkl', 'rb'))

series1 = TimeSeries.from_dataframe(data, 'datetime', 'CO(GT)')
series2 = TimeSeries.from_dataframe(data, 'datetime', 'T')

his_ex1 = model1.historical_forecasts(
    series1, start=pd.Timestamp('2004-03-18 00:00:00'))
his_ex2 = model2.historical_forecasts(
    series2, start=pd.Timestamp('2004-03-18 00:00:00'))

# def predictionCO(dt, tm):

#     dt = str(dt)
#     if tm / 10 == 0:
#         tm = str(tm)
#         tm = tm = "0" + tm + ":00:00"
#     else:
#         tm = str(tm)
#         tm = tm+":00:00"
#     dite = dt + str(' ') + tm
#     date_time_obj = datetime.datetime.strptime(dite, '%Y-%m-%d %H:%M:%S')
#     #dite = pd.to_datetime(dite.strip(), format='%Y-%m-%d %H.%M.%S')
#     #dite = Datetime.Parse(dite, '%Y-%m-%d %H.%M.%S')
#     #dite = pd.to_datetime(dite.strip(), format='%Y-%m-%d %H.%M.%S')
#     #dite = pd.Timedelta.to_pytimedelta(dite)
#     CO = model1.predict(date_time_obj)
#     return CO


def predictionCO(dt):
    begin = (dt-18)*24
    end = begin + 24
    return np.array(his_ex1[begin: end])


st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 350px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 350px;
        margin-left: -350px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title('Air Quality Prediction')
st.sidebar.subheader("amsmskdmd")

app_mode = st.sidebar.selectbox('Choose the App mode',
                                ['Prediction', 'Forecast']
                                )


if app_mode == 'Prediction':
    st.markdown(
        """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    dt = st.date_input(
        "Select a date",
        datetime.date(2004, 3, 18), datetime.date(2004, 3, 18), datetime.date(2004, 3, 24))
    #18, 3, 2004
    dt = dt.day

    if st.button("Predict CO"):
        #output = predictionCO(dt)
        #st.success('CO amount is {}'.format(output))
        plt.figure(101, figsize=(12, 8))
        st.line_chart(his_ex1)
        #his_ex1.plot(label='forecast-fft', lw=3)
        plt.legend()


elif app_mode == 'Forecast':
    st.set_option('deprecation.showfileUploaderEncoding', False)
    Start = st.sidebar.button('Plotttt')

    st.sidebar.markdown('---')
    st.markdown(
        """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
        width: 400px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
        width: 400px;
        margin-left: -400px;
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("Get, set and Readyyyy!!")
