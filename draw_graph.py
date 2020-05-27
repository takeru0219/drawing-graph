from io import BytesIO

import urllib

import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
matplotlib.use('Agg')

import numpy as np

def plot_graph(
    range_x,
    range_y,
    draw_range_x,
    draw_range_y,
    formura_list,
    point_list
    ):
    x = np.linspace(0,10)
    y = np.sin(x)
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(x,y)
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    return png_output.getvalue()
