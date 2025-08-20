# app.py  — run a Dash site from your existing figures without editing them
import os
from importlib.machinery import SourceFileLoader
from types import ModuleType

import dash
from dash import dcc, html

# ---- Load your existing script AS-IS (file with double dot) ----
MODULE_PATH = "shenlei_dashboard..py"   # keep your filename unchanged
module: ModuleType = SourceFileLoader("shenlei_dashboard_module", MODULE_PATH).load_module()

# Collect figures that your script created (if a fig is missing, skip gracefully)
fig_names = ["fig1", "fig2", "fig3", "fig4"]
figs = []
for name in fig_names:
    fig = getattr(module, name, None)
    if fig is not None:
        figs.append((name.upper(), fig))

# Fallback message if no figures found
content = (
    [html.Div(
        "No Plotly figures detected. Ensure your script defines fig1, fig2, fig3, fig4.",
        style={"color":"#fff","padding":"20px","fontFamily":"Orbitron, monospace"}
    )]
    if not figs else
    [html.Div([
        html.H3(title, style={"color":"#00F5FF","fontFamily":"Orbitron, monospace"}),
        dcc.Graph(figure=fig, style={"height":"85vh"})   # preserve your layout look
    ], style={"marginBottom":"30px"}) for title, fig in figs]
)

# ---- Dash app / server for Render ----
app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server  # <- Render/Heroku entrypoint

app.layout = html.Div(
    content,
    style={
        "backgroundColor": "#0A0A1A",
        "padding": "20px",
        "minHeight": "100vh"
    }
)

if __name__ == "__main__":
    app.run_server(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=False)
