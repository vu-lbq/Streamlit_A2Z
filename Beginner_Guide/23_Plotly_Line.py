import streamlit as st
import pandas as pd
import plotly.express as px

# Data Set
data = pd.read_csv("./files/avocado.csv")

# Minimizing Dataset
albany_df = data[data['region']=="Albany"]
al_df = albany_df[albany_df["year"]==2015]

#Line
line_chart = px.line(
    x = al_df["Date"],
    y = al_df["Large Bags"]
)

#Change Color
line_chart.update_traces(line_color = "yellow")
st.header("Line Chart")
st.plotly_chart(line_chart)