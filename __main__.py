import os

import tornado.httpserver
import tornado.ioloop
import tornado.log
import tornado.web
from tornado.options import define, options, parse_command_line

import config
import handlers.web
import handlers.api

class Application(tornado.web.Application):
    def __init__(self, debug):
        routes = [
            # Web handlers
            (r"/", handlers.web.ExampleWebHandler),

            # API handlers
            (r"/api", handlers.api.ExampleApiHandler),

            # Public files: JS, CSS, images and favicon.ico
            (r'/public/(.*)', tornado.web.StaticFileHandler, {
                'path' : os.path.join(os.path.dirname(__file__), "public")
            }),
            (r'/(favicon\.ico)', tornado.web.StaticFileHandler, {
                "path": os.path.join(os.path.dirname(__file__), "public", "images")
            })
        ]

        settings = {
            "template_path": os.path.join(os.path.dirname(__file__), "templates"),
            "debug": debug,
            "cookie_secret": config.cookie_secret,
            "xsrf_cookies": True,
            "login_url": '/login'
        }

        tornado.web.Application.__init__(self, routes, **settings)

    @property
    def logger(self):
        return tornado.log.app_log

if __name__=='__main__':
    define('port', default = config.port, help = 'port', type = int)
    define('debug', default = False, help = 'run in debug mode', type = bool)
    parse_command_line()

    app = Application(options.debug)
    app.logger.info('Starting %s on 0.0.0.0:%s' % ('tornado skeleton', options.port))

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

