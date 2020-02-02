from flask import Flask, render_template
import numpy
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from io import BytesIO
import base64


app = Flask(__name__)

@app.route('/graph/<x>')
def hello_world(x):
    ### Generating X,Y coordinaltes to be used in plot
    X = numpy.linspace(0,10,30)
    Y = X**int(x)
    ### Generating The Plot
    plt.plot(X,Y)
    ### Saving plot to disk in png format
    plt.savefig('static/images/square_plot.png')
    #plt.savefig('/tmp/square_plot.png')

    ### Rendering Plot in Html
    figfile = BytesIO()
    plt.savefig(figfile, format='png')
    plt.close()
    figfile.seek(0)
    figdata_png = base64.b64encode(figfile.getvalue())
    result = figdata_png
    return render_template('output.html', result=result)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
