#!/usr/bin/perl -wT 
use CGI ':standard';
use CGI::Carp qw(warningsToBrowser fatalsToBrowser); 

use strict;
print "Content-type: text/html\n\n";

print "<!DOCTYPE html>";

print "<html><head>";
print qq(<link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Audiowide">);

print "<title>Perl Demo</title></head>";

print "<body>";
print qq(<div style="color:blue;font-size:5em;text-align:center;font-family: 'Audiowide', sans-serif;">); 
print "This is my first Perl program\n<br>";



print "</div></body></html>";
