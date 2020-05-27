from io import BytesIO

from flask import Flask, render_template

import urllib
import matplotlib
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
matplotlib.use('Agg')

import numpy as np

app = Flask(__name__)

@app.route('/image')
def plot_graph(image):
    x = numpy.linspace(0,10)
    y = numpy.sin(x)
    fig = Figure()
    ax = fig.add_subplot(111)
    ax.plot(x,y)
    canvas = FigureCanvasAgg(fig)
    png_output = BytesIO()
    canvas.print_png(png_output)
    img_data = urllib.parse.quote(png_output.getvalue())
    return img_data


@app.route('/')
def index():
    return render_template('index.html', img_data = None)

if __name__ == "__main__":
    app.run(debug=True, port = 9999)