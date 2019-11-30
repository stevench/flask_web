# -*- encoding: utf-8 -*-
from jinja2 import Markup
from pyecharts import options as opts
from pyecharts.charts import Bar
from app.echarts import echarts_bp

def bar_base():
    c = (Bar()
         .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
         .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
         .add_yaxis("商家B", [15, 25, 16, 55, 48, 8])
         .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
         )
    return c


@echarts_bp.route("/bar")
def bar():
    c = bar_base()
    return Markup(c.render_embed())
