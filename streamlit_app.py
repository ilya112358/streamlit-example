from bokeh.embed import file_html
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


df = pd.read_csv('data.csv')
p = figure(title='Right Ankle Angles', x_axis_label='Gait cycle, %', y_axis_label='Degrees')
colors = ['red', 'green', 'blue', 'orange', 'black']
for walk in range(1, len(df.columns)):
    p.line('Gait cycle', df.columns[walk], source=ColumnDataSource(df), legend_label=df.columns[walk], color=colors[walk-1])

st.title("Check Bokeh Library")
st.text("before using it")
components.html(file_html(p, 'cdn', ), height=600)
