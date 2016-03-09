from .. import basehandler


class WebBaseHandler(basehandler.BaseHandler):
    def prepare(self):
        """prepare function: it is called after initialize function"""
        pass


authenticated = basehandler.authenticated
run_asynchronous = basehandler.run_asynchronous
