import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts


check = st.selectbox(
    'Select the Events to see the Event Related Data',
    ('Apple', 'Microsoft', 'Google',"UHC-Healthcare","Wipro-Internal","Cisco","United-Airlines"))
st.subheader(":blue[Spending done in Individual Team]:")

if check == 'Apple':
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Apple",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Servicing-Developement"},
                    {"value": 600, "name": "Product Development"},
                    {"value": 1100, "name": "Testing"},
                    {"value": 1050, "name": "Containers"},
                    {"value": 500, "name": "Product-Testing"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 6000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="800px")
elif check == "Microsoft":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Microsoft",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Servicing-Developement"},
                    {"value": 600, "name": "Product Development"},
                    {"value": 1100, "name": "Testing"},
                    {"value": 1050, "name": "Containers"},
                    {"value": 500, "name": "Product-Testing"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 2000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px")
elif check == "Google":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Google",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Crawling-Team"},
                    {"value": 600, "name": "Indexing-Team"},
                    {"value": 1100, "name": "Deployment-Team"},
                    {"value": 1050, "name": "Development-Team"},
                    {"value": 500, "name": "Product-Testing"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 25000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)
    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px")
elif check == "UHC-Healthcare":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "UHC-Healthcare",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Data-Analysis"},
                    {"value": 600, "name": "Data-Engineer"},
                    {"value": 1100, "name": "Prediction-Team"},
                    {"value": 1050, "name": "Claim-Approval-team"},
                    {"value": 500, "name": "Support-Team"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 6000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px") 

elif check == "Wipro-Internal":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Wipro-Internal",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Manual-testing-Team"},
                    {"value": 600, "name": "Automation-Testing "},
                    {"value": 1100, "name": "Portal-Development"},
                    {"value": 1050, "name": "Server-Maintenance"},
                    {"value": 500, "name": "Medical-Claims"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 9000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="900px") 


elif check == "Cisco":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "Cisco",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Networking-Team"},
                    {"value": 600, "name": "Devops-team"},
                    {"value": 1100, "name": "Analysis-team"},
                    {"value": 1050, "name": "Onsite-development"},
                    {"value": 500, "name": "Offshore-testing"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 8000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px") 

elif check == "United-Airlines":
    options = {
        "tooltip": {"trigger": "item"},
        "legend": {"left": "0%", "right": "0%", "Top": "0%","Bottom":"10%"},
        "series": [
            {
                "name": "United-Airlines",
                "type": "pie",
                "radius": "50%",
                "data": [
                    {"value": 1000, "name": "Algorithm-Development-Team"},
                    {"value": 600, "name": "Device-Analysis"},
                    {"value": 1100, "name": "Black-Box-Testing"},
                    {"value": 1050, "name": "Validation-Team"},
                    {"value": 500, "name": "Onsite-Developement"},
                ],
                "emphasis": {
                    "itemStyle": {
                        "shadowBlur": 10,
                        "shadowOffsetX": 0,
                        "shadowColor": "rgba(0, 0, 0, 0.5)",
                    }
                },
                "label": {
                    "formatter": "{b}: {d}%"
                    },
            }
        ],
    }

    # Add a Streamlit slider to control the pie chart
    slider_value = st.slider("Control the slider to see the changes in the Volunteer Contributions for the Event", 0, 6000, 0, 100)
    st.write("Contribution for "+check+">= ",slider_value)

    # Filter the data based on the slider value
    filtered_data = [data for data in options["series"][0]["data"] if data["value"] >= slider_value]

    # Update the data for the pie chart with the filtered data
    options["series"][0]["data"] = filtered_data
    st.divider()
    st_echarts(options=options, height="600px")  
    
hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
