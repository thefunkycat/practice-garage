import webapp2

from handlers import handler


app = webapp2.WSGIApplication([
    ('/', handler.WorkerHandler),
    ('/(.*)', handler.WorkerHandler)
    ], debug=True)