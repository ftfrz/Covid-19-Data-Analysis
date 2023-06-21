import streamlit as st
from pages import show_home_page, show_global_trends_page, show_country_analysis_page, show_comparison_analysis_page, show_map_view_page, show_about_page

def main():
    st.set_page_config(layout="wide")
    st.title('COVID-19 Analysis')
    st.sidebar.title('Navigation')
    pages = ['🏠Home', '🌍Global Trends', '☂️Country Analysis', '📊Comparison Analysis', '🗺️Map View', '📝About']
    page = st.sidebar.radio('Go to',pages)

    if page == '🏠Home':
        show_home_page()

    elif page == '🌍Global Trends':
        show_global_trends_page()

    elif page == '☂️Country Analysis':
        show_country_analysis_page()

    elif page == '📊Comparison Analysis':
        show_comparison_analysis_page()

    elif page == '🗺️Map View':
        show_map_view_page()

    elif page == '📝About':
        show_about_page()

if __name__ == "__main__":
    main()
