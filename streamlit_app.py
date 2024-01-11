from bokeh.embed import file_html
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.tools import PanTool, WheelZoomTool
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
# import g4f

# response = g4f.ChatCompletion.create(
#     model="gpt-3.5-turbo",
#     messages=[{"role": "user", "content": "Hello"}],
#     stream=True,
# )
# for message in response:
#     print(message, flush=True, end='')

df = pd.read_csv('data.csv')
p = figure(title='Right Ankle Angles', 
           x_axis_label='Gait cycle, %', 
           y_axis_label='Degrees', 
           height=400,
           width=600)
p.title.align = "center"
p.title.text_font_size = "25px"
p.border_fill_color = "seashell"
# p.toolbar.active_drag = p.select_one(PanTool)
p.toolbar.active_drag = None
p.toolbar.active_scroll = p.select_one(WheelZoomTool)
colors = ['red', 'green', 'blue', 'orange', 'black']
lines, labels = [], []
for col in range(1, len(df.columns)-1):
    line = p.line('Gait cycle', df.columns[col], source=ColumnDataSource(df), color=colors[col-1])
    lines.append(line)
    labels.append((df.columns[col], [line]))
# lines[-1].glyph.line_width = 2
legend = Legend(items=labels, location="center")
legend.orientation = "horizontal"
legend.border_line_color = "black"
p.add_layout(legend, 'above')

st.title("Check Bokeh Library")
st.text("before using it")
components.html(file_html(p, 'cdn', ), height=400, width=600)
