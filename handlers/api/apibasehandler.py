import functools
import json

import jsonschema
import tornado.web

from .. import basehandler


class ApiBaseHandler(basehandler.BaseHandler):
    def check_xsrf_cookie(self):
        pass

    def prepare(self):
        """prepare function: it is called after initialize function"""
        if self.request.headers.get("Content-Type", "").startswith("application/json"):
            try:
                self.json_args = json.loads(self.request.body, encoding="utf-8")
            except ValueError:
                raise tornado.web.HTTPError(400, "JSON is not valid")

    def write_json_response(self, dictionary, cacheable = False):
        self.set_header("Content-Type", "application/json")
        self.set_header("Cache-Control", "public, no-transform, max-age=300" if cacheable else "no-cache")
        self.write(json.dumps(dictionary, default = lambda o: o.__dict__, encoding='utf-8'))

def validate_json(schema):
    #Decorate methods with this to validate input json.
    def decorator(method):
        @functools.wraps(method)
        def wrapper(self, *args, **kwargs):
            if self.json_args is None:
                raise tornado.web.HTTPError(403, "No JSON data received")

            try:
                jsonschema.validate(self.json_args, schema)
            except jsonschema.ValidationError as e:
                raise tornado.web.HTTPError(403, e.message)

            return method(self, *args, **kwargs)
        return wrapper
    return decorator


authenticated = basehandler.authenticated
run_asynchronous = basehandler.run_asynchronous
