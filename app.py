import socket
from wsgiref.simple_server import make_server
from renderer import render
from views import main_view


HOST, PORT = '', 8000
print('Serving HTTP on port {}'.format(PORT))


URLS = {
	'/': main_view,
}


def parse_request(environ):
	method = environ['REQUEST_METHOD']
	url = environ['PATH_INFO']
	url = url.replace('favicon.ico', '')
	return (method, url)


def generate_headers(method, url):

	if not url in URLS:
		return ([('Content-type', 'text/html')], '404 Not Found')

	methods = ['GET', 'POST']

	if method not in methods:
		return ([('Content-type', 'text/html')], '405 Method Not Allowed')
                
	return ([('Content-type', 'text/html')], '200 OK')


def generate_content(environ, method, status, url):
    if status == '404 Not Found':
        return b'<h1>404</h1><p>Not Found</p>'

    if status == '405 Method Not Allowed':
        return b'<h1>405</h1><p>Method Not Allowed</p>'
                
    return URLS[url](environ, method)


def web_app(environ, response):
	method, url = parse_request(environ)
	headers, status = generate_headers(method, url)
	response(status, headers)
	body = generate_content(environ, method, status, url)

	return [body]


with make_server(HOST, PORT, web_app) as server:
	server.serve_forever()

