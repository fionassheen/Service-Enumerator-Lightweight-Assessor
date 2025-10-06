from jinja2 import Environment, FileSystemLoader
import json, os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), 'templates')

def make_report(data, out_html='report.html'):
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    tpl = env.get_template('report.html')
    data['open_count'] = len(data.get('open_ports', []))
    rendered = tpl.render(data=data, data_raw=json.dumps(data, indent=2))
    with open(out_html, 'w') as f:
        f.write(rendered)
    return out_html
