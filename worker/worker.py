import webapp2

from handlers import handler


app = webapp2.WSGIApplication([
    ('/worker/', handler.WorkerHandler),
    ('/worker/(.*)', handler.WorkerHandler)
    ], debug=True)