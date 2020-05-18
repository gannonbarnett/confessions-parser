from flask import Flask, Response, render_template 
from flask import Response

from analytics import Analytics
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
MAY_2020_DATA_PATH = "data_5_2020.csv"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/word_freq/<word>/plot.png')
def generate_plot(word):
    fig = AnalObj.createDailyFigure(*AnalObj.getWordFreqData(word))
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":     
    AnalObj = Analytics(MAY_2020_DATA_PATH)
    app.run(debug=True)
