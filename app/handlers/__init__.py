""" Override file to make read params easier
"""


from webapp2 import RequestHandler
from webapp2_extras import jinja2
from app.system.params import ParamCollection

class BasicHandler(RequestHandler):
    
    def initialize(self, request, response):
        super(BasicHandler, self).initialize(request, response)
        self.params = ParamCollection(self.request)

    def jinja(self):
        return jinja2.get_jinja2(app=self.app)

    def render_response(self, _template, **tv):
        """ tv = template value
            add like: a="a", b="c", c={"id": 8240285}
            or
            tv = {"a": "a",  "b":"c", c:{"id": 8240285}}
            **tv
        """
        rv = self.jinja().render_template(_template, **tv)
        self.response.write(rv)

    def render_json(self, data):
        self.response.headers['Content-Type'] = 'application/json; charset=utf-8'
        self.response.write(data)

    def render_json_ok(self):
        response = {
            'status': {
                'code': 200,
                'message': 'Success',
            },
            'response': {}
        }
        self.render_json(response)
