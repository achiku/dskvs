# -*- coding: utf-8 -*-
import os
import json

from werkzeug.exceptions import HTTPException
from werkzeug.routing import Map, Rule
from werkzeug.wrappers import Response, Request

from loader import create_data


class Dskvs(object):

    def __init__(self, config):
        self.data_file_path = config['data_file_path']
        self.internal_data = create_data(self.data_file_path)
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
        l = self.internal_data[key]
        return Response(json.dumps(l), 'application/json')

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)


def create_app():
    data_file_path = os.path.join(
        os.path.dirname(os.path.abspath(os.path.dirname(__file__))), 'data', 'data.tsv')
    app = Dskvs({'data_file_path': data_file_path})
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5001, app, use_debugger=True, use_reloader=True)
