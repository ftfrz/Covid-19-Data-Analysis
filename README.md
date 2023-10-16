# Covid-19-Data-Analysis

<div align="center">
 <img src="https://cdn.mathpix.com/snip/images/Bxg4ceomxCnysNVZKjVg9AuwZJurq8uljdceAw4qQT8.original.fullsize.png" width="450"/>
</div>

## Project Overview
"Covid-19-Data-Analysis" is a data-driven web application that provides up-to-date and comprehensive information about the global COVID-19 pandemic. It visualizes global trends, individual country analyses, and comparison analyses. The application also features a map view to illustrate the worldwide spread of the pandemic. The statistical data is extracted from CSV files containing global confirmed, death, and recovery cases.
<table>
  <tr>
    <td>
      <img src="https://cdn.mathpix.com/snip/images/m7KJpwsnXHq0H1mWtUPNNTiO9G6lZDfZRHcOyv8HAVI.original.fullsize.png" alt="Image 1" width="400">
    </td>
    <td style="text-align: center;">
      Home Page
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://cdn.mathpix.com/snip/images/uFsxb_7oPiMjLS9P__hrf2BleBQs1FkclxWP5OwVrhg.original.fullsize.png" alt="Image 2" width="400">
    </td>
    <td style="text-align: center;">
      Comprehensive Analysis of Global Trends
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://cdn.mathpix.com/snip/images/3r3gwyspO8pXeFd_zfP8ob310--4XDEr2BTH5xUG8IQ.original.fullsize.png" alt="Image 3" width="400">
    </td>
    <td style="text-align: center;">
      Interactive Map View
    </td>
  </tr>
</table>


## Video Demo
See [Video Demo(in Chinese)](https://www.capcut.cn/share/7247485648234353931?t=1)

## How to Run the Project
1. Clone the repository or download the files onto your local machine.
2. Ensure you have Python 3.7+ installed.
3. Navigate to the project directory in your terminal.
4. Install the necessary dependencies using pip:
   ```sh
   pip install -r requirements.txt
   ```
5. Run the Streamlit application:
   ```sh
   streamlit run main.py
   ```
6. The application should now be running at `http://localhost:8501`.

## Required Libraries
The project uses the following Python libraries:
- pandas
- numpy
- plotly
- streamlit
- geopandas
- altair
- streamlit_extras

All libraries can be installed via pip using the `requirements.txt` file.


## Running the Project
All necessary files, including the code and data sources, are included in the project repository. If you encounter any issues, please open an issue in the project's GitHub repository.

# About Covid-19-Data-Analysis

## Features
1. **Global and Country-Specific Analysis:** Get a detailed overview of the global situation and delve into the specifics of each country. Understand the daily number of confirmed cases, deaths, and recoveries.

2. **Comparison Analysis:** Compare the COVID-19 situation across different countries. View daily confirmed cases, mortality rate, and recovery rate distribution for the countries most affected by the pandemic.

3. **Map View:** Visualize the spread of COVID-19 worldwide through an interactive map view that shows confirmed cases and deaths.


## Data Sources
The data used by this application is derived from CSV files provided by [Johns Hopkins CSSE](https://github.com/CSSEGISandData/COVID-19#covid-19-data-repository-by-the-center-for-systems-science-and-engineering-csse-at-johns-hopkins-university). The geographic information is obtained from [Natural Earth](https://www.naturalearthdata.com/downloads/10m-cultural-vectors/).

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/Namenameee/Covid-19-Data-Analysis/LICENSE) file for details. 

## Acknowledgements
We extend our deepest gratitude to all healthcare workers, researchers, and everyone on the front lines combating the virus. This project is a tribute to their tireless efforts and sacrifices.



