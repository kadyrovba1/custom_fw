import socket
from renderer import render
from views import main_view


PORT = 9090
print('Serving HTTP on port {}'.format(PORT))


URLS = {
	'/': main_view,
}


def parse_request(env):
	method = env['REQUEST_METHOD']
	url = env['PATH_INFO']
	url = url.replace('favicon.ico', '')
	return (method, url)


def generate_headers(method, url):

	if not url in URLS:
		return ([('Content-Type', 'text/html')], '404 Not Found')

	methods = ['GET', 'POST']

	if method not in methods:
		return ([('Content-Type', 'text/html')], '405 Method Not Allowed')
                
	return ([('Content-Type', 'text/html')], '200 OK')


def generate_content(env, method, status, url):
    if status == '404 Not Found':
        return b'<h1>404</h1><p>Not Found</p>'

    if status == '405 Method Not Allowed':
        return b'<h1>405</h1><p>Method Not Allowed</p>'
                
    return URLS[url](env, method)


def application(env, start_response):
	method, url = parse_request(env)
	headers, status = generate_headers(method, url)
	start_response(status, headers)
	body = generate_content(env, method, status, url)

	return [body]

