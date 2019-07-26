import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content=Type'] = 'text/plain'
        self.response.write('Hello, Wrod')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

class SecretPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'html'
        self.response.write('<h1> You found the secret! </h1>')

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/secret', SecretPage)
], debug=True)
