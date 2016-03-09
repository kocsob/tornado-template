import webbasehandler

class ExampleWebHandler(webbasehandler.WebBaseHandler):
    def get(self):
        self.render('index.html')

    def post(self):
        username = self.get_argument('username', default=None)
        if username:
            self.write("Welcome %s!" % username)
        else:
            self.write("Hello world")
