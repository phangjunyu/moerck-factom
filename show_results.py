from bokeh.io import save, output_file
from bokeh.models import ColumnDataSource
import bokeh.palettes as bp
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

def results_html(results):
    output_file("templates/results.html")
    candidates = []
    counts = []
    for candidate, count in results.items():
        candidates.append(candidate)
        counts.append(count)

    source = ColumnDataSource(data=dict(candidates=candidates, counts=counts))

    p = figure(x_range=candidates, plot_height=300, toolbar_location=None, title="Vote Count")
    p.vbar(x='candidates', top='counts', width=1, source=source, legend="candidates",
           line_color='white', fill_color=factor_cmap('candidates', palette=bp.Spectral10, factors=candidates))

    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.y_range.end = round(max(counts), -1) if max(counts) > 10 else max(counts)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"

    save(p)
