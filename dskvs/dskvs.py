# -*- coding: utf-8 -*-
import os
from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response, Request


class Dskvs(object):

    def __init__(self, config):
        self.data_file_path = config['data_file_path']
        self.url_map = Map([
            Rule('/<schema>/<key>', endpoint='get_list'),
        ])

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def on_get_list(self, request, schema, key):
        return Response('{0}.{1}'.format(schema, key), 'text/json')

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    data_file_path = os.path.join(os.path.dirname(__file__), 'data')
    app = Dskvs({'data_file_path': data_file_path})
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5001, app, use_debugger=True, use_reloader=True)
