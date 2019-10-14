#UTF-8
#python3.7
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.animation as animation
from IPython.display import HTML

df = pd.read_csv('数据地址', usecols=['name', 'group', 'year', 'value'])

fig.ax = plt.subplots(figsize=(15, 8))

def draw_barchart(year):
    dff = df[df['year'].eq(year)].sort_values(by='value', ascending=True).tail(10)
    ax.clear()
    ax.barh(dff['name'], diff['value'], color=[colors[group_lk[x]] for x in diff['name']])
    dx = diff['value'].max() / 200
    