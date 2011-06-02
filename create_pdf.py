import os
import sys
from jinja2 import Environment, FileSystemLoader
from ho import pisa

current_dir = os.path.dirname(__name__)
template_path = os.path.abspath(os.path.join(current_dir, 'templates'))
jinja_env = Environment(loader=FileSystemLoader(template_path))

def render_to_pdf(template, filename='out.pdf'):
    data = dict(small=range(10), large=range(200))
    html = str(jinja_env.get_template(template).render(data))
    with open(filename, 'wb') as doc:
        pdf = pisa.CreatePDF(html, doc)
        if not pdf.err:
            pisa.startViewer(filename)

if __name__ == '__main__':
    render_to_pdf(sys.argv[1])