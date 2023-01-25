#!/usr/bin/ruby
print "Content-type: text/html\n\n"


require 'cgi'

cgi = CGI.new
puts "<div style=\"color:red;font-size:3em;text-align:center;\">Your city is " + cgi['city'].capitalize + "</div>"
puts "<div style=\"color:red;font-size:3em;text-align:center;\">Your province is " + cgi['province'].capitalize + "</div>"
puts "<div style=\"color:red;font-size:3em;text-align:center;\">Your country is " + cgi['country'].capitalize + "</div>"
puts "<img src=" + cgi['url'] + " width=100%>"
