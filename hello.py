def wsgi_application(environ, start_response):
   # бизнес логика
   status = '200 OK'
   headers = [
	('Content-Type', 'text/plain')
]
   body = '\r\n'.join(environ ['QueryString'].split('&'))
   start_response(status, headers)
   return [body]
