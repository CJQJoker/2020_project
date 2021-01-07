import pyecharts.options as opts
from pyecharts.charts import WordCloud
from ciyun import counts

items = list(counts.items())  # 转换成列表形式
items.sort(key=lambda x: x[1], reverse=True)  # 按次数排序
(
    WordCloud()
    .add(series_name="词云", data_pair=items, word_size_range=[6, 66], width=850, height=450)
    .set_global_opts(
        title_opts=opts.TitleOpts(
            title="词云", title_textstyle_opts=opts.TextStyleOpts(font_size=23)
        ),
        tooltip_opts=opts.TooltipOpts(is_show=True),
    )
    .render("词云.html")
)