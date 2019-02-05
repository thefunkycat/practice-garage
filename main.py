import webapp2
from webapp2_extras import jinja2
from jinja2 import PackageLoader
from app.handlers.garages import Garages


class MainPage(webapp2.RequestHandler):

    def jinja(self):
        config = {
            'environment_args': {
                'loader': PackageLoader('app', 'templates')
            }
        }
        return jinja2.Jinja2(app=self.app, config=config)

    def render_response(self, _template, **tv):
        """ tv = template value
            add like: a="a", b="c", c={"id": 8240285}
            or
            tv = {"a": "a",  "b":"c", c:{"id": 8240285}}
            **tv
        """
        rv = self.jinja().render_template(_template, **tv)
        self.response.write(rv)

    def get(self):
        self.render_response("index.html")


app = webapp2.WSGIApplication([
    ('/', MainPage),

    ('/garages', Garages),
    ('/garages/(.*)', Garages)
    ], debug=True)
