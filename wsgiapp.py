def app(environ, start_response):
    #Minimalist WSGI application
    status = '200 OK'
    response_headers = [('content-Type', 'text/plain')]
    start_response(status, response_headers)
    return [b'This is a small WSGI app that doesn\'t use any of the popular frameworks!\n']
