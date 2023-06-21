import plotly.express as px
import geopandas as gpd
from data_loading import load_data, load_data2
import pandas as pd
import numpy as np
import streamlit as st

def plot_map(df, title):
    world = gpd.read_file('world_map.shp')
    country_total = df.iloc[:, -1]
    world = world.set_index('NAME').join(country_total.rename(title))
    # Convert to numeric and handle non-numeric values
    world[title] = pd.to_numeric(world[title], errors='coerce')

    # Now compute average, ignoring NaN values
    color_continuous_midpoint = np.average(world[title], weights=world[title])
    fig = px.choropleth(world.reset_index(), locations='NAME',
                        locationmode='country names', color=title,
                        hover_name='NAME', projection="natural earth",
                        hover_data=[title], title=title,
                        color_continuous_scale='Inferno',
                        color_continuous_midpoint=np.average(world[title], weights=world[title]))

    # Change layout
    fig.update_layout(
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        coloraxis_colorbar={
            'title': title,
        },
    )
    return fig
    pass

def show_home_page():
    from streamlit_extras.let_it_rain import rain
    rain(
        emoji="🎈",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    # 添加介绍
    st.write('👋Welcome to our website! ')
    st.write(
        'Here, we provide the analysis results of global and national COVID-19 data 📊, including cumulative confirmed 😷, death 💀 and recovery 😇 cases, as well as mortality rate and recovery rate. We hope 🙏 this information can help you better understand the global situation of COVID-19. Stay safe, stay informed! 🧡')
    st.write('👈 Please select a page on the left sidebar to start exploring!')
    confirmed_df, deaths_df, recovered_df = load_data()
    st.header('🏠Home')

    # Calculate global statistics
    global_confirmed = confirmed_df.iloc[:, 4:].sum().max()
    global_deaths = deaths_df.iloc[:, 4:].sum().max()
    global_recovered = recovered_df.iloc[:, 4:].sum().max()

    # Display global statistics
    st.subheader('Global Statistics')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<h2 style="color: black;text-align: center;">Total Confirmed </h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 40px; color: blue;text-align: center;">{global_confirmed}</p>',
                    unsafe_allow_html=True)
    with col2:
        st.markdown(f'<h2 style="color: black;text-align: center;">Total Deaths</h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 40px; color: red;text-align: center;">{global_deaths}</p>',
                    unsafe_allow_html=True)
    with col3:
        st.markdown(f'<h2 style="color: black;text-align: center;">Total Recovered </h2>', unsafe_allow_html=True)
        st.markdown(f'<p style="font-size: 40px; color: green;text-align: center;">{global_recovered}</p>',
                    unsafe_allow_html=True)


def show_global_trends_page():
    confirmed_df, deaths_df, recovered_df = load_data()
    import plotly.express as px

    st.header('🌍Global Trends')

    # Calculate global daily confirmed, deaths and recovered cases
    global_daily_confirmed = confirmed_df.iloc[:, 4:].sum(axis=0)
    global_daily_deaths = deaths_df.iloc[:, 4:].sum(axis=0)
    global_daily_recovered = recovered_df.iloc[:, 4:].sum(axis=0)

    # Convert the index to datetime format and sort the data by index
    global_daily_confirmed.index = pd.to_datetime(global_daily_confirmed.index)
    global_daily_deaths.index = pd.to_datetime(global_daily_deaths.index)
    global_daily_recovered.index = pd.to_datetime(global_daily_recovered.index)
    global_daily_confirmed = global_daily_confirmed.sort_index()
    global_daily_deaths = global_daily_deaths.sort_index()
    global_daily_recovered = global_daily_recovered.sort_index()

    # 找到数据开始缺失的日期
    missing_data_start_date = global_daily_recovered[global_daily_recovered == 0].index.min()

    # 只使用数据开始缺失日期之前的数据
    global_daily_recovered = global_daily_recovered[global_daily_recovered.index < missing_data_start_date]

    # Calculate global daily new cases
    global_daily_new_cases = global_daily_confirmed.diff()

    # Plot global daily confirmed cases
    st.subheader('Global Daily Confirmed Cases')
    fig = px.line(global_daily_confirmed.reset_index(), x='index', y=0,
                  labels={'index': 'Date', 0: 'Confirmed Cases'})
    st.plotly_chart(fig)

    # Plot global daily deaths
    st.subheader('Global Daily Deaths')
    fig = px.line(global_daily_deaths.reset_index(), x='index', y=0, labels={'index': 'Date', 0: 'Deaths'})
    st.plotly_chart(fig)

    # Plot global daily recovered cases
    st.subheader('Global Daily Recovered Cases')
    fig = px.line(global_daily_recovered.reset_index(), x='index', y=0,
                  labels={'index': 'Date', 0: 'Recovered Cases'})
    st.plotly_chart(fig)

    # Plot global daily new cases
    st.subheader('Global Daily New Cases')
    fig = px.line(global_daily_new_cases.reset_index(), x='index', y=0, labels={'index': 'Date', 0: 'New Cases'})
    st.plotly_chart(fig)

def show_country_analysis_page():
    confirmed_df, deaths_df, recovered_df = load_data2()
    import plotly.express as px

    st.header('☂️Country Analysis')

    # Get the list of countries
    countries = confirmed_df['Country/Region'].unique()

    # Let the user select a country
    country = st.selectbox('👇Select a country', countries)

    # Get the data for the selected country
    country_data_confirmed = confirmed_df[confirmed_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    country_data_deaths = deaths_df[deaths_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)
    country_data_recovered = recovered_df[recovered_df['Country/Region'] == country].iloc[:, 4:].sum(axis=0)

    # 找到数据开始缺失的日期
    missing_data_start_date2 = country_data_recovered[country_data_recovered == 0].index.min()

    # 只使用数据开始缺失日期之前的数据
    country_data_recovered = country_data_recovered[country_data_recovered.index < missing_data_start_date2]

    # Convert the index to datetime format and sort the data by index
    country_data_confirmed.index = pd.to_datetime(country_data_confirmed.index)
    country_data_deaths.index = pd.to_datetime(country_data_deaths.index)
    country_data_recovered.index = pd.to_datetime(country_data_recovered.index)
    country_data_confirmed = country_data_confirmed.sort_index()
    country_data_deaths = country_data_deaths.sort_index()
    country_data_recovered = country_data_recovered.sort_index()

    # Calculate the mortality rate and recovery rate for the selected country
    country_mortality_rate = country_data_deaths.iloc[-1] / country_data_confirmed.iloc[-1]
    country_recovery_rate = country_data_recovered.iloc[-1] / country_data_confirmed.iloc[-1]

    # Display the mortality rate and recovery rate
    st.write(f'Mortality rate in {country}: {country_mortality_rate:.2%}')
    st.write(f'Recovery rate in {country}: {country_recovery_rate:.2%}')

    # Plot the data for the selected country
    st.subheader(f'Daily Confirmed Cases in {country}')
    fig = px.line(country_data_confirmed.reset_index(), x='index', y=0,
                  labels={'index': 'Date', 0: 'Confirmed Cases'})
    st.plotly_chart(fig)

    st.subheader(f'Daily Deaths in {country}')
    fig = px.line(country_data_deaths.reset_index(), x='index', y=0, labels={'index': 'Date', 0: 'Deaths'})
    st.plotly_chart(fig)

def show_comparison_analysis_page():
    import altair as alt
    confirmed_df, deaths_df, recovered_df = load_data()
    st.header('📊Comparison Analysis')

    # Calculate the total confirmed cases for each country
    country_total_confirmed = confirmed_df.iloc[:, 4:].sum(axis=1)

    # Remove countries with zero confirmed cases
    country_total_confirmed = country_total_confirmed[country_total_confirmed > 0]

    # Get the top 5 countries with the most confirmed cases
    top_countries = country_total_confirmed.nlargest(5).index

    # Plot the daily confirmed cases for the top 5 countries
    st.subheader('Daily Confirmed Cases in Top 5 Countries')

    # Create an empty DataFrame to store data for all top countries
    all_countries_data = pd.DataFrame()

    for i in top_countries:
        country_data = confirmed_df.loc[i].iloc[4:]
        country_data.index = pd.to_datetime(country_data.index)
        country_data = country_data.sort_index()

        # Add country name as a column
        country_data_df = pd.DataFrame({
            'date': country_data.index,
            'cases': country_data.values,
            'country': i
        })
        # Append the data to the all_countries_data DataFrame
        all_countries_data = all_countries_data.append(country_data_df)

    # Hover selection
    hover = alt.selection_single(
        fields=["date"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    # Create line chart
    lines = alt.Chart(all_countries_data, height=500).mark_line().encode(
        x=alt.X('date:T', title="Date"),
        y=alt.Y('cases:Q', title="Cases"),
        color='country:N'
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(all_countries_data)
        .mark_rule()
        .encode(
            x="yearmonthdate(date)",
            y="cases",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("date", title="Date"),
                alt.Tooltip("cases", title="Cases"),
            ],
        )
        .add_selection(hover)
    )

    # Combine the chart components
    chart = (lines + points + tooltips).interactive()
    st.altair_chart(chart, use_container_width=True)
    import altair as alt

    # Calculate the recovery rate for each country
    country_recovery_rate = recovered_df.sum(axis=1) / confirmed_df.sum(axis=1)

    # Remove inf and NaN values
    country_recovery_rate = country_recovery_rate.replace([np.inf, -np.inf], np.nan)
    country_recovery_rate = country_recovery_rate.dropna()

    # Create a DataFrame for Altair
    data = pd.DataFrame({
        'Country': country_recovery_rate.index,  # use the index of the DataFrame
        'Recovery Rate': country_recovery_rate.values
    })

    # Plot the distribution of recovery rate
    st.subheader('Distribution of Mortality and Recovery Rate in Different Countries')

    # Create an Altair chart
    chart = alt.Chart(data).mark_circle().encode(
        alt.X("Country:N", title="Country"),
        alt.Y("Recovery Rate:Q", title="Recovery Rate"),
    ).properties(
        title='Distribution of Recovery Rate of COVID-19 in Different Countries'
    )
    st.altair_chart(chart, use_container_width=True)

    from streamlit_extras.altex import bar_chart

    # Calculate the total confirmed cases, deaths, and recoveries for each country
    total_confirmed = confirmed_df.sum(axis=1)
    total_deaths = deaths_df.sum(axis=1)
    total_recovered = recovered_df.sum(axis=1)

    # Calculate the mortality rate and recovery rate for each country
    mortality_rate = total_deaths / total_confirmed
    recovery_rate = total_recovered / total_confirmed

    # Select the top 10 countries with the highest total confirmed cases
    top_countries = total_confirmed.nlargest(10).index

    # Create a DataFrame that includes the mortality rate and recovery rate for these countries
    data = pd.DataFrame({
        'Country': np.repeat(top_countries, 2),  # repeat each country name twice
        'Rate Type': np.tile(['Mortality Rate', 'Recovery Rate'], len(top_countries)),
        # alternate between 'Mortality Rate' and 'Recovery Rate'
        'Rate': np.concatenate([mortality_rate.loc[top_countries].values, recovery_rate.loc[top_countries].values])
        # first all mortality rates, then all recovery rates
    })

    # Create a grouped bar chart
    bar_chart(
        data=data,
        x="Rate Type:O",
        y="Rate:Q",
        color="Rate Type:N",
        column="Country:N",
        title="Mortality Rate and Recovery Rate for Top 10 Countries with Highest Confirmed Cases",
        width=60,
        use_container_width=False,
    )

def show_map_view_page():
    st.header('🗺️Map View')
    confirmed_df, deaths_df, recovered_df = load_data()
    fig_confirmed = plot_map(confirmed_df, 'Confirmed')
    fig_deaths = plot_map(deaths_df, 'Deaths')
    st.plotly_chart(fig_confirmed)
    st.plotly_chart(fig_deaths)



def show_about_page():
    from streamlit_extras.let_it_rain import rain
    rain(
        emoji="❤️",
        font_size=54,
        falling_speed=5,
        animation_length="infinite",
    )
    st.header('📝About')
    st.write('🌐Welcome to our Covid-19 data analysis platform! ')
    st.write('🧠We are dedicated to providing up-to-date and comprehensive information about the Covid-19 pandemic. Our goal is to help you understand the current situation and make informed decisions. ')
    st.write('🙏We would like to express our deepest gratitude to all the healthcare workers 👩‍⚕️👨‍⚕️ and researchers 👩‍🔬👨‍🔬 who are working tirelessly to combat this virus. ')
    st.write('😊Thanks for using our platform! Your support means a lot to us. ')
    st.write('Data Source: [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19#covid-19-data-repository-by-the-center-for-systems-science-and-engineering-csse-at-johns-hopkins-university) 📊')
    st.write('Geographic Information: [Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/)🌍')
