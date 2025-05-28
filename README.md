# API-Intergration

**COMPANY**: CODTECH IT SOLUTION

**NAME**: ALLEN SAM AJI

**INTERN ID**: CT08DL1122

**DURATION**: 8 WEEKS

**MENTOR**: NEELA SANTOSH

# DESCRIPTION OF TASK LIKE HOW YOU PERFORMED AND WHAT YOU HAVE DONE AND PASTE PICTURES OF OUTPUT

# 🌦️ Weather Dashboard – API Integration and Data Visualization

## Overview
This project demonstrates how to integrate a public API using Python and visualize real-time weather data. It fetches 5-day weather forecasts using the **OpenWeatherMap API** and creates visualizations using **Matplotlib** and **Seaborn**.

---

## Features
- 🌐 Connects to OpenWeatherMap public API using `requests`
- 📊 Visualizes temperature and humidity over time
- 📅 Converts UNIX timestamps to readable date-time
- 🛡️ Includes error handling for invalid responses and network issues

---

## Technologies Used
- **Python 3**
- **Requests** (API calls)
- **Matplotlib** (data plotting)
- **Seaborn** (enhanced visualization)
- **OpenWeatherMap API**
- **JSON**

---

## How to Run

1. Clone the repo or download the script.
2. Install required libraries:
   ```bash
   pip install requests matplotlib seaborn

#Objective
The objective of this task was to integrate a public API into a Python application and visualize the fetched data using Python data visualization libraries such as Matplotlib or Seaborn. This is a common real-world task that demonstrates backend integration with frontend data representation. For this purpose, we chose the OpenWeatherMap API, which provides comprehensive weather data in JSON format.

#Implementation Process
We began by signing up for an OpenWeatherMap developer account and obtained a free API key, which is required to access the forecast endpoint. The Python requests library was used to construct and send a GET request to the API. We built the request URL dynamically using parameters like the city name (London by default), the API key, and units (metric for Celsius).

After receiving the JSON response from the API, we implemented error handling to check for invalid keys, city names, or network issues. We also added checks to ensure the response contained the expected data before proceeding. This avoids program crashes from malformed or unexpected data.

We then extracted relevant data from the response: timestamps (dt), temperature (temp), and humidity (humidity). The UNIX timestamps were converted into human-readable datetime objects using Python's datetime module. These were stored in lists that were then passed into plotting functions.

For the visualization part, we used Seaborn and Matplotlib. Two line plots were created:

Temperature over time: Showed how the temperature varies across the forecasted period.

Humidity over time: Displayed the percentage of humidity during the same timeframe.

These visualizations were placed side-by-side using Matplotlib's subplotting feature. Labels, legends, and titles were added to ensure the graphs are intuitive and easy to interpret. We formatted the x-axis labels to show date and time and rotated them for better readability.

During the process, we encountered a Unicode encoding error due to emojis in print statements on Windows terminals. This was caused by the default Windows character encoding (cp1252), which does not support Unicode emojis. To resolve this, we removed the emojis from print() statements to ensure compatibility.

#Conclusion
This task demonstrated the complete process of accessing a public API, extracting meaningful data, and visualizing it effectively using Python. It required knowledge of working with HTTP requests, JSON parsing, data cleaning, and plotting. Real-world problems such as error handling, invalid inputs, and character encoding issues were encountered and resolved. The final script can be easily extended or modified to accept user input, change units, or even support other types of data like wind speed or pressure.

The project serves as a great example of combining Python programming, data handling, and visual storytelling through code. It’s a useful starting point for developers interested in building dashboards or working with external APIs in Python.

#Example Output
The script opens a visualization window with two side-by-side plots:

Left Plot: Temperature vs Time

Right Plot: Humidity vs Time



#License
This project is free to use and modify for educational purposes.

