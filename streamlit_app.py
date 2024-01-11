from bokeh.embed import file_html
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Legend
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
p = figure(title='Right Ankle Angles', x_axis_label='Gait cycle, %', y_axis_label='Degrees')
p.title.align = "center"
p.title.text_font_size = "25px"
colors = ['red', 'green', 'blue', 'orange', 'black']
lines, labels = [], []
for walk in range(1, len(df.columns)):
    line = p.line('Gait cycle', df.columns[walk], source=ColumnDataSource(df), color=colors[walk-1])
    lines.append(line)
    labels.append((df.columns[walk], [line]))
lines[-1].glyph.line_width = 2
legend = Legend(items=labels, location="center")
legend.orientation = "horizontal"
legend.border_line_color = "black"
p.add_layout(legend, 'above')

st.title("Check Bokeh Library")
st.text("before using it")
components.html(file_html(p, 'cdn', ), height=600)
