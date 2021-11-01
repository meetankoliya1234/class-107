import pandas as pd
from pandas.core import groupby
import plotly.graph_objects as go

df = pd.read_csv('./data.csv')
studentdf = df.loc[df['student_id'] == 'TRL_987']
print(studentdf.groupby('level')['attempt'].mean())

fig = go.Figure(go.Bar(
    x = studentdf.groupby('level')['attempt'].mean(),
    y = ['level1', 'level 2', 'level 3', 'level 4'],
    orientation = 'h'
))

fig.show()