import show_results
import FinalCount as fc
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/results')
def get_results():
    fn = fc.FinalCount()
    results = fn.countFinalTally()

    show_results.results_html(results)
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
