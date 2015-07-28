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

class HomePageHandler(webapp2.RequestHandler):
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

        greeting = users.create_login_url('/homepage')
        self.response.write(template.render({"greeting":greeting}))


class buddyRequest(ndb.Model):
    activity = ndb.StringProperty()
    time = ndb.TimeProperty()
    date = ndb.DateProperty()
    place = ndb.StringProperty()
    other = ndb.StringProperty()



class CreateHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/createform.html')
        self.response.write(template.render({}))


    def post(self):
        date_js = self.request.get("date")
        logging.info(type(date_js))
        date = datetime.datetime.fromtimestamp(date_js/1000)
        buddyRequest_object = buddyRequest(activity = self.request.get("activity"),
                                           time = self.request.get("time"),
                                           date = date,
                                           place = self.request.get("place"),
                                           other = self.request.get("other"),
                                           )
        buddyRequest_object.put()










jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/homepage', HomePageHandler),
    ('/create', CreateHandler),



], debug=True)
