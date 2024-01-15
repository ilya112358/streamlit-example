from bokeh.embed import file_html
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Legend
# from bokeh.models.tools import PanTool, WheelZoomTool
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd

df = pd.read_csv('data.csv')
p = figure(title='Right Ankle Angles', 
           x_axis_label='Gait cycle, %', 
           y_axis_label='Degrees', 
           height=400,
           width=600,
           tools = "box_zoom,reset",
           tooltips = "[$name] @$name{0.0} at @{Gait cycle}")
p.title.align = "center"
p.title.text_font_size = "25px"
p.border_fill_color = "seashell"

colors = ['red', 'green', 'blue', 'orange', 'black']
lines, labels = [], []
for col in range(1, len(df.columns)):
    line = p.line('Gait cycle', df.columns[col], source=ColumnDataSource(df), color=colors[col-1], name=df.columns[col])
    lines.append(line)
    labels.append((df.columns[col], [line]))
lines[-1].glyph.line_width = 2
legend = Legend(items=labels, location="center")
legend.orientation = "horizontal"
legend.border_line_color = "black"
p.add_layout(legend, 'above')

st.title("Check Bokeh Library")
st.text("before using it")
components.html(file_html(p, 'cdn', ), height=400, width=600)
df