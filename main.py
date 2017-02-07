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
import caesar
import cgi #common gateway interface

def build_page(textarea_content):
    rot_label="<label>Rotate by:</label>"
    rotation_input="<input type='number' name='rotation'/>"

    message_label="<label>Type a message:</label>"
    textarea="<textarea name='message'>" + textarea_content + "</textarea>"

    submit="<input type='submit'/>"
    form=("<form method='post'>" +
            rot_label + rotation_input + "<br>" +
            message_label + textarea + "<br>" +
            submit + "</form>")

    header="<h2>Web Caesar</h2>"

    return header + form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        #message='Helloooooo, world!!!!'
        #encrypted_message=caesar.encrypt(message, 13)
        content=build_page("")
        #string above is blank because user just arrived and we want it to be blank
        self.response.write(header + form)

    def post(self):
        message=self.request.get("message") #hello</textarea>hello
        rotation=int(self.request.get("rotation")) #0
        encrypted_message=caesar.encrypt(message, rotation) #hello</textarea>hello - is passed to helper function: build page
        escaped_message = cgi.escape(encrypted_message) #looks like this: #hello&lt;/textarea&gt;hello
        content=build_page(escaped_message) #escaped variable is passed into content 
        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
