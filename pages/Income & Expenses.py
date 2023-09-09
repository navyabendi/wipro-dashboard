import streamlit as st
from streamlit_echarts import st_echarts
from pyecharts import options as opts
from pyecharts.charts import Pie, Timeline
from streamlit_echarts import st_pyecharts
import pandas as pd
import pandas as pd
import numpy as np
import random


st.subheader("Wipro Income in Different Quarters for the past Years")

# Define the ECharts options
options = {
    "legend": {},
    "tooltip": {},
    "dataset": {
        "source": [
            ['product', '2018', '2019', '2020', '2021','2022'],
            ['Quarter 1', 41.1, 30.4, 65.1, 53.3, 88.3],
            ['Quarter 2', 86.5, 92.1, 85.7, 83.1, 87.3],
            ['Quarter 3', 24.1, 67.2, 79.5, 86.4, 67.8],
            ['Quarter 4', 34.1, 76.2, 94.5, 68.4, 73.9]
        ]
    },
    "xAxis": [
        {"type": 'category', "gridIndex": 0},
        {"type": 'category', "gridIndex": 1}
    ],
    "yAxis": [{"gridIndex": 0}, {"gridIndex": 1}],
    "grid": [{"bottom": '55%'}, {"top": '55%'}],
    "series": [
        # These series are in the first grid.
        {"type": 'bar', "seriesLayoutBy": 'row'},
        {"type": 'bar', "seriesLayoutBy": 'row'},
        {"type": 'bar', "seriesLayoutBy": 'row'},
        {"type": 'bar', "seriesLayoutBy": 'row'},
        # These series are in the second grid.
        {"type": 'bar', "xAxisIndex": 1, "yAxisIndex": 1},
        {"type": 'bar', "xAxisIndex": 1, "yAxisIndex": 1},
        {"type": 'bar', "xAxisIndex": 1, "yAxisIndex": 1},
        {"type": 'bar', "xAxisIndex": 1, "yAxisIndex": 1},
        {"type": 'bar', "xAxisIndex": 1, "yAxisIndex": 1}

    ]
}

# Render the ECharts chart using streamlit_echarts
st_echarts(options, height=500)

st.divider()

st.header("Year wise Expenses")

# Define data
attr = ["Salaries", "Office Expenses", "Employee Benifits", "Maintenance", "Other Expenses"]
# Replace the following values with your own data for each year
values_2018 = [100, 200, 150, 300, 120]
values_2019 = [120, 150, 180, 250, 110]
values_2021 = [80, 120, 250, 180, 90]
values_2022 = [200, 180, 160, 280, 150]
values_2023 = [150, 220, 170, 260, 100]

tl = Timeline()

# Create Pie charts for each year in the timeline
for i, values in zip(range(2018, 2023), [values_2018, values_2019, values_2021, values_2022, values_2023]):
    pie = (
        Pie()
        .add(
            "Check",
            [list(z) for z in zip(attr, values)],
            rosetype="radius",
            radius=["30%", "55%"],
            label_opts=opts.LabelOpts(formatter="{b}: {d}%"),  # Display category name and percentage
        )
        .set_global_opts(title_opts=opts.TitleOpts("{}".format(i)))
    )
    tl.add(pie, "{}".format(i))

# Render the Pie chart timeline using st_echarts
st_pyecharts(tl, height=500)

if st.checkbox("Show Data Table"):
    st.subheader("Year-wise Expenses Data")
    for i, values in zip(range(2018, 2023), [values_2018, values_2019, values_2021, values_2022, values_2023]):
        st.write(str(i))
        st.write(pd.DataFrame({"Categories": attr, "Expenses": values}))

hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
