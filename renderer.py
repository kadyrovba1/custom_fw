from jinja2 import Template


def render(file_name, context=None):
    with open(file_name, 'r') as html_file:
        html = html_file.read()
        if context:
            template = Template(html)
            html = template.render(context)
        return html
