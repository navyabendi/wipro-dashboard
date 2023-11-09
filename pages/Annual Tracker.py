import streamlit as st
import pandas as pd
import numpy as np
from streamlit_echarts import st_echarts
import random


st.header("Quarterly Finance details of the Year For the Wipro")

# Sample data for two years: 2022 and 2023
data_2022 = {
    'source': [
        ['product', 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'],
        ['Income', 80.5, 87.1, 82.7, 79.1],
        ['Profit', 36.1, 25.4, 60.1, 48.3],
        ['Loss', 22.1, 63.2, 75.5, 82.4],
        ['Networth', 51.2, 63.1, 65.2, 68.4]
    ]
}

data_2023 = {
    'source': [
        ['product', 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'],
        ['Income', 86.5, 92.1, 85.7, 83.1],
        ['Profit', 41.1, 30.4, 65.1, 53.3],
        ['Loss', 24.1, 67.2, 79.5, 86.4],
        ['Networth', 55.2, 67.1, 69.2, 72.4]
    ]
}

data_2024 = {
    'source': [
        ['product', 'Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4'],
        ['Income', 864.5, 92.1, 865.7, 863.1],
        ['Profit', 415.1, 30.4, 65.1, 563.3],
        ['Loss', 124.1, 67.2, 769.5, 866.4],
        ['Networth', 565.2, 667.1, 69.2, 762.4]
    ]
}
# Function to get the selected year data
def get_selected_year_data(selected_year):
    if selected_year == 2022:
        return data_2022
    elif selected_year == 2023:
        return data_2023
    elif selected_year == 2024:
        return data_2024
    
option = {
    'baseOption': {
        'timeline': {
            'axisType': 'category',
            'autoPlay': False,
            'playInterval': 1000,
            'data': ['2022', '2023','2024'],
            'label': {
                'formatter': '{value}'
            }
        },
        'legend': {},
        'tooltip': {},
        'series': [
            {
                'type': 'pie',
                'radius': '30%',
                'center': ['25%', '30%'],
                'title': {
                    'text': 'Quarter 1',
                },
            },
            {
                'type': 'pie',
                'radius': '30%',
                'center': ['75%', '30%'],
                'title': {
                    'text': 'Quarter 2',
                    'left': 'center'
                },
                'encode': {
                    'itemName': 'product',
                    'value': 'Quarter 2'
                }
            },
            {
                'type': 'pie',
                'radius': '30%',
                'center': ['25%', '75%'],
                'title': {
                    'text': 'Quarter 3',
                    'left': 'center'
                },
                'encode': {
                    'itemName': 'product',
                    'value': 'Quarter 3'
                }
            },
            {
                'type': 'pie',
                'radius': '30%',
                'center': ['75%', '75%'],
                'title': {
                    'text': 'Quarter 4',
                    'left': 'center'
                },
                'encode': {
                    'itemName': 'product',
                    'value': 'Quarter 4'
                }
            }
        ]
    },
    'options': [
        {
            'title': {'text': '2022'},
            'dataset': get_selected_year_data(2022),
            'series': [
                {'encode': {'itemName': 'product', 'value': 'Quarter 1'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 2'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 3'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 4'}}
            ]
        },
        {
            'title': {'text': '2023'},
            'dataset': get_selected_year_data(2023),
            'series': [
                {'encode': {'itemName': 'product', 'value': 'Quarter 1'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 2'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 3'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 4'}}
            ]
        },
        {
            'title': {'text': '2024'},
            'dataset': get_selected_year_data(2024),
            'series': [
                {'encode': {'itemName': 'product', 'value': 'Quarter 1'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 2'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 3'}},
                {'encode': {'itemName': 'product', 'value': 'Quarter 4'}}
            ]
        }
    ]
}

st_echarts(option, height=600)

st.divider()

options = {
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["2023","2022", "2021", "2020", "2019", "2018"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["Quarter1", "Quarter2", "Quarter3", "Quarter4"],
    },
    "yAxis": {"type": "value"},
    "series": [
                {
            "name": "2023",
            "type": "line",
            "stack": "Total",
            "data": [100000, 200000, 400000, 500000],
        },
        {
            "name": "2022",
            "type": "line",
            "stack": "Total",
            "data": [600000, 700000, 800000, 500000],
        },
        {
            "name": "2021",
            "type": "line",
            "stack": "Total",
            "data": [300000, 400000, 500000, 700000],
        },
        {
            "name": "2020",
            "type": "line",
            "stack": "Total",
            "data": [500000, 300000, 500000, 300000],
        },
        {
            "name": "2019",
            "type": "line",
            "stack": "Total",
            "data": [500000, 700000, 400000, 200000],
        },
        {
            "name": "2018",
            "type": "line",
            "stack": "Total",
            "data": [700000, 400000, 500000, 600000],
        },
    ],
}
st_echarts(options=options, height="400px")

st.subheader("Growth Rate Over Years")

# Code of showing the Metrics Of the Monthly Funds

twenty,twentyone,twentytwo,twentythree = st.columns(4)

twenty.metric(label="2020", value="47850", delta="250 %")
twentyone.metric(label="2021", value="30300", delta="-44.9 %")
twentytwo.metric(label="2022", value="17600", delta="-53.02 %")
twentythree.metric(label="2023", value="4400", delta="0",delta_color="off")


