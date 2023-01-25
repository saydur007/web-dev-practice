#!/usr/bin/perl
use CGI ':standard';
print "Content-type: text/html\n\n";

$first = param ('first');
print "Hello $first";