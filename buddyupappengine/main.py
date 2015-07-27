#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import logging
import jinja2
import os
from google.appengine.api import users
import urllib2
import json
from google.appengine.ext import ndb
import datetime

class TitlePageHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('homepage.html')

        user = users.get_current_user()

        if user:
            logout =  users.create_logout_url('/')
            self.response.write(template.render({"logout":logout,
                                                 "user": user,
                                                }))


        else:
            self.response.write("you are signed out")




class MainHandler(webapp2.RequestHandler):
    def get(self):

        template = jinja_environment.get_template('titlepage.html')


        user = users.get_current_user()

        greeting = users.create_login_url('/titlepage')
        self.response.write(template.render({"greeting":greeting}))

class CreateHandler(webapp2.RequestHandler):
    def post(self):
        template = jinja_environment.get_template('templates/createform.html')
        self.response.write(template.render({}))




jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/titlepage', TitlePageHandler),
    ('/create', CreateHandler)


], debug=True)
