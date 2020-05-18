from flask import Flask, Response, render_template, request
from flask import Response

from analytics import Analytics
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)
DATA_SOURCE = "data_5_2020.csv"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/plot.png')
def generate_plot():
    # todo change design to support multiple types of queiries, not just word freq analysis.. 
    word_freq_targets = request.args.get('wf')
    show_num = request.args.get('show_num') == 'true'
    use_avg = request.args.get('use_avg') == 'true'
    fig = AnalObj.createBaseDailyFigure()
    fig = AnalObj.addWordFrequency(fig, word_freq_targets.split(","), color='blue', use_avg=use_avg)
    if (show_num):
        fig = AnalObj.addNumLine(fig)
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')

if __name__ == "__main__":     
    AnalObj = Analytics(DATA_SOURCE)
    app.run(debug=True)
