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
    activity = ndb.StringProperty(required=True)
    time = ndb.StringProperty(required=True)
    date = ndb.StringProperty(required=True)
    place = ndb.StringProperty(required=True)
    other = ndb.StringProperty()
    buddies = ndb.StringProperty(repeated=True)
    buddies_users = ndb.StringProperty(repeated=True)
    creator = ndb.StringProperty(required=True)
    date_created =  ndb.DateTimeProperty()




class CreateHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('templates/createform.html')
        user = users.get_current_user()
        if user:
            logout =  users.create_logout_url('/')
            self.response.write(template.render({"logout":logout,
                                                 "user": user,
                                                }))
        else:
            self.response.write("you are signed out")


    def post(self):
        date_js = self.request.get("date")
        date = str(date_js)
        user = users.get_current_user()
        buddyRequest_object = buddyRequest(activity = self.request.get("activity"),
                                           time = self.request.get("time"),
                                           date = date,
                                           place = self.request.get("place"),
                                           other = self.request.get("other"),
                                           creator = user.nickname(),
                                           buddies = [user.nickname()],
                                           buddies_users = [],
                                           date_created = datetime.datetime.now()
                                           )
        buddyRequest_object.put()
        self.redirect('/view')


class ViewHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        template = jinja_environment.get_template('viewevents.html')

        if user:
            query = buddyRequest.query()
            query = query.order(-buddyRequest.date)
            data = query.fetch()
            logout =  users.create_logout_url('/')
            self.response.write(template.render({"logout":logout,
                                                 'data':data,
                                                 'user':user.nickname()
                                                }))
        else:
            self.response.write("you are signed out")


    def post(self):
        request_id = buddyRequest.get_by_id(int(self.request.get("requestid")), parent=None)
        request_id.key.delete()
        user = users.get_current_user()
        query = buddyRequest.query()
        data = query.fetch()
        template = jinja_environment.get_template('viewevents.html')
        self.response.write(template.render({'data':data,
                                             'user':user.nickname()
                                            }))


class AddsignIn(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('titlepage.html')
        user = users.get_current_user()
        greeting = users.create_login_url('/add?requestid='+self.request.get('requestid'))
        self.response.write(template.render({"greeting":greeting}))


class AddyouselfHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_environment.get_template('addpage.html')

        current_user = users.get_current_user()
        requestid = int(self.request.get('requestid'))
        buddy_request = buddyRequest.get_by_id(requestid, parent=None)
        self.response.write(template.render({"requestid":requestid,
                                             "current_user":current_user.nickname(),
                                             "buddy_request":buddy_request,
                                            }))
    def post(self):
        current_user = users.get_current_user()
        requestid = int(self.request.get('requestid'))
        buddy_request = buddyRequest.get_by_id(requestid, parent=None)
        buddy_request.buddies.append(self.request.get('fname'))
        buddy_request.buddies_users.append(current_user.nickname())
        buddy_request.put()
        template = jinja_environment.get_template('buddyadded.html')
        self.response.write(template.render({"requestid":requestid}))

class BuddieslistHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        template = jinja_environment.get_template('buddies.html')

        if user:
            query = buddyRequest.query()
            query = query.order(-buddyRequest.date_created)
            data = query.fetch()
            logout =  users.create_logout_url('/')
            self.response.write(template.render({"logout":logout,
                                                 'data':data,
                                                 'user':user.nickname()
                                                }))
        else:
            self.response.write("you are signed out")






jinja_environment = jinja2.Environment(loader =
    jinja2.FileSystemLoader(os.path.dirname(__file__)))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/homepage', HomePageHandler),
    ('/create', CreateHandler),
    ('/view', ViewHandler),
    ('/add', AddyouselfHandler),
    ('/addsignin', AddsignIn),
    ('/buddies', BuddieslistHandler),




], debug=True)
