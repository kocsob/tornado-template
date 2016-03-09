import apibasehandler

class ExampleApiHandler(apibasehandler.ApiBaseHandler):
    def post(self):
        username = self.get_argument('username', default=None)
        if username:
            self.write_json_response({'message': "Welcome %s!" % username})
        else:
            self.write({'message': "Hello world"})
