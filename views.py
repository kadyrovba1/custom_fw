import re

from cgi import parse_qs
from renderer import render
from db_manager import create_query
from tasks import send_link_mail


def main_view(env, method):
    template = 'index.html'
    if method == "POST":
        try:
            request_body_size = int(env.get('CONTENT_LENGTH', 0))
        except (ValueError):
            request_body_size = 0
        request_body = env['wsgi.input'].read(request_body_size)
        data = parse_qs(request_body)

        link = data[b'link'][0].decode()
        email = data[b'email'][0].decode()
        create_query(link, email)
        send_link_mail(email, link)
       
    response = render(template).encode('utf-8')
    return response
    