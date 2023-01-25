#!/usr/bin/python

import cgi, cgitb 

form = cgi.FieldStorage() 
city = form.getvalue('city')
province  = form.getvalue('province')
country  = form.getvalue('country')
url  = form.getvalue('url')
print "Content-type:text/html\n\n"

print '<html><body>'
print '<div style="font-size:3em;color:#cc0000;text-align:center;">City: %s Province: %s Country: %s</div>' % (city.upper(), province.upper(), country.upper())

print '<img src= %s' % (url)
print ' width=80% style="border:5px solid blue;">'

print '</body></html>'



