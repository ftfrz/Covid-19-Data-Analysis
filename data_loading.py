import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
    deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
    recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

    confirmed_df = confirmed_df.fillna(0)
    deaths_df = deaths_df.fillna(0)
    recovered_df = recovered_df.fillna(0)

    country_daily_confirmed = confirmed_df.groupby('Country/Region').sum().iloc[:, 2:]
    country_daily_deaths = deaths_df.groupby('Country/Region').sum().iloc[:, 2:]
    country_daily_recovered = recovered_df.groupby('Country/Region').sum().iloc[:, 2:]

    country_daily_confirmed.columns = pd.to_datetime(country_daily_confirmed.columns)
    country_daily_deaths.columns = pd.to_datetime(country_daily_deaths.columns)
    country_daily_recovered.columns = pd.to_datetime(country_daily_recovered.columns)

    return country_daily_confirmed, country_daily_deaths, country_daily_recovered

@st.cache_data
def load_data2():
    confirmed_df = pd.read_csv('time_series_covid19_confirmed_global.csv')
    deaths_df = pd.read_csv('time_series_covid19_deaths_global.csv')
    recovered_df = pd.read_csv('time_series_covid19_recovered_global.csv')

    confirmed_df = confirmed_df.fillna(0)
    deaths_df = deaths_df.fillna(0)
    recovered_df = recovered_df.fillna(0)

    return confirmed_df, deaths_df, recovered_df
