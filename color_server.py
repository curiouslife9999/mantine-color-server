import logging
from pathlib import Path
from dash import Dash, html
import dash_mantine_components as dmc

logging.basicConfig(format='%(asctime)s [%(name)s:%(lineno)d] [%(levelname)s] %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(Path(__file__).name)

# Initialize the app
asset_dir = Path(Path(__file__).parent.parent, 'assets')
app = Dash('color_server', update_title=None, title='Mantine Colors', assets_folder=str(asset_dir))
server = app.server

color_divs = []
for name in dmc.theme.DEFAULT_COLORS:
    texts = [dmc.Text(name, style={'font-weight': 'bold', 'font-size': '24px', 'text-align': 'center'})]
    for color in dmc.theme.DEFAULT_COLORS[name]:
        texts.append(dmc.Text(color, style={'background': color,
                                            'font-weight':"bold",
                                            'font-size': '20px',
                                            "text-align":"center",
                                            'width': '150px',
                                            'height': '30px'}))
    div = html.Div(texts, style={'display': 'flex', 'flex-direction': 'column'})
    color_divs.append(div)

app.layout = dmc.MantineProvider(children=[
    dmc.Paper(children=[
        html.Div(color_divs, style={'display': 'flex', 'flex-direction': 'row'}),
    ], style={'font-size': 12, 'padding': 0})
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=9001, debug=True)
