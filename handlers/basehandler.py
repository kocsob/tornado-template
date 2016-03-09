import functools
import threading

import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    @property
    def logger(self):
        return self.application.logger

    def initialize(self):
        """initialize database connection: it is called before prepare function"""
        pass

def run_asynchronous(method):
    @functools.wraps(method)
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target = method, args = args, kwargs = kwargs)
        thread.start()
        return thread
    return wrapper

authenticated = tornado.web.authenticated
