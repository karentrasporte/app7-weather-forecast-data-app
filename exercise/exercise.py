import streamlit as st
import plotly.express as px
import pandas as pd

# Create web page details
st.title("In Search for Happiness")
x_axis_label = st.selectbox("Select the data for X-axis",
                      ("GDP","Happiness","Generosity") )
y_axis_label = st.selectbox("Select the data for Y-axis",
                      ("GDP","Happiness","Generosity") )
st.subheader(f"{x_axis_label} and {y_axis_label}")

df = pd.read_csv("exercise/happy.csv")

if x_axis_label == "GDP":
    x_axis_value = df["gdp"]
if x_axis_label == "Happiness":
    x_axis_value = df["happiness"]
if x_axis_label == "Generosity":
    x_axis_value = df["generosity"]

if y_axis_label == "GDP":
    y_axis_value = df["gdp"]
if y_axis_label == "Happiness":
    y_axis_value = df["happiness"]
if y_axis_label == "Generosity":
    y_axis_value = df["generosity"]

figure = px.scatter(x=x_axis_value, y=y_axis_value, labels={"x":x_axis_label,"y":y_axis_label})
st.plotly_chart(figure)