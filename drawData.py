import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Scatter
from pyecharts.commons.utils import JsCode

data = pd.read_excel("G:\data_2.xls", sheet_name="data")

for i in range(len(data)):
    s = data.loc[i, 'date']
    while s[-1] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        s = s[:-1]
    s = s.replace('年', '-').replace('月', '-').replace('日', '-')
    data.loc[i, 'date'] = pd.to_datetime(s, format="%Y-%m-%d-%H:%M")

x = []
for i in data.loc[:,["date"]].values.tolist():
    x.append(i[0])
y = []
for i in data.loc[:,["chicknum"]].values.tolist():
    y.append(int(i[0]))

(
    Scatter(init_opts=opts.InitOpts(width="1600px", height="1000px"))
    .add_xaxis(xaxis_data=x)
    .add_yaxis(
        series_name="",
        y_axis=y,
        symbol_size=20,
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_series_opts()
    .set_global_opts(
        xaxis_opts=opts.AxisOpts(
            type_="time", splitline_opts=opts.SplitLineOpts(is_show=True)
        ),
        yaxis_opts=opts.AxisOpts(
            type_="value",
            axistick_opts=opts.AxisTickOpts(is_show=True),
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
        tooltip_opts=opts.TooltipOpts(is_show=False),
    )
    .render("basic_scatter_chart.html")
)