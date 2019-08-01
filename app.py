import re
import os
from renderer import render
from views import main_view

URLS = {
	'/': main_view,
}

def parse_request(env):
	method = env['REQUEST_METHOD']
	url = env['PATH_INFO']
	match = re.search(r'mp3/?$', url)
	filename = False
	if match:
		filename = url.replace('http://127.0.0.1:9090', '')
		filename = filename.replace('%20', ' ')
		url = match.group(0)
		return (env, method, url, filename)
	return (env, method, url, filename)


def mp3_serve(env, start_response, filename):
	current_dir = os.getcwd()
	filepath = current_dir + filename
	mimetype = 'application/x-mplayer2'
	size = os.path.getsize(filepath)
	headers = [('Content-Type', mimetype), ('Content-Length', str(size))]
	start_response('200 OK', headers)
	return send_file(filepath, size)
	

def send_file(filepath, size):
	BLOCK_SIZE = 4096
	fh = open(filepath, 'rb')
	while True:
		block = fh.read(BLOCK_SIZE)
		if not block:
			fh.close()
			break
		yield block


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
	env, method, url, filename = parse_request(env)
	if filename is not False:
		return mp3_serve(env, start_response, filename)
	headers, status = generate_headers(method, url)
	start_response(status, headers)
	body = generate_content(env, method, status, url)

	return [body]

