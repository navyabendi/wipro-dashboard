import streamlit as st

from pyecharts import options as opts
from pyecharts.charts import Graph
from streamlit_echarts import st_pyecharts
from pyecharts import options as opts
from pyecharts.charts import WordCloud

st.set_page_config(
    page_title="Wipro-Dashboard",
    page_icon="wipro_emoji.jpeg",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.subheader("Welcome to the Wipro Finance Dashboard ")


def main():

    nodes = [
        {"name": "Conda", "symbolSize": 50},
        {"name": "Python", "symbolSize": 50},
        {"name": "streamlit", "symbolSize": 50},
        {"name": "Github(CI/CD)", "symbolSize": 50},
        {"name": "Echarts/pyecharts", "symbolSize": 50},
        {"name": "Matplotylib", "symbolSize": 50},
        {"name": "Google APIs", "symbolSize": 50},
        {"name": "Pandas", "symbolSize": 50},
        {"name": "Finaces", "symbolSize": 50},

    ]
    
    links = []
    for i in nodes:
        for j in nodes:
            links.append({"source": i.get("name"), "target": j.get("name")})

    c = (
        Graph()
        .add("", nodes, links, repulsion=8000)
        .set_global_opts(title_opts=opts.TitleOpts(title="Below are the tools used to build this application"))
    )
    
    st_pyecharts(c, height = 500)

st.markdown('I am **:green[ Navya]**, I am here to present my project MVP of Finacial System Of wipro under the Gudiance of **:green[Dr.Prasant Kumar]**')
st.markdown('A **:blue[financial dashboard portal(MVP)]** built using Streamlit would be a solution to this problem. Streamlit is a Python framework that allows you to create interactive web applications. A financial dashboard portal built using Streamlit would be easy to use and would present the data in a way that is easy to understand. It would facilitate the decision-making of companies regarding their financial situation.')


if __name__ == "__main__":
    main()


st.subheader('Features') 
# The Financial Dashboard Portal will consist of the following main features:


st.markdown('**:blue[Home]**')
st.markdown('The Home section will serve as the landing page and provide an overview of the portals capabilities and its importance for Wipros financial management.')

st.markdown('**:blue[Investment & Expenses]**')
st.markdown('Detailed information on the organizations investment and expenditure will be displayed in this section. Interactive Charts showing historical trends will be included, enabling users to analyze the finance patterns')
st.markdown('**:blue[Annual and Monthly Tracker]**')
st.markdown('Tracking and comparing financial performance on an annual basis shall be the focus of the Annual Tracker section. Each year/Month, users will be able to look at the Growth rate of the key financial metrics.')
st.markdown('**:blue[Projects Budgets]**')
st.markdown('Details on the financial situation of existing projects will be provided in the Projects Budgets section. For each project, it will cover the allocation of resources, real expenditure, and variance analysis.')



hide_st_style = """
<style>
#Mainmenu {Visibility : hidden;}
footer {Visibility : hidden;}
header {Visibility : hidden;}
</style>
"""
st.markdown(hide_st_style,unsafe_allow_html=True)
