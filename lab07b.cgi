#!/usr/bin/perl
use CGI ':standard';
print "Content-type: text/html\n\n";

$first = param ('first');
$last = param ('last');
$street = param ('street');
$city = param ('city');
$province = param ('province');
$post = param ('post');
$phone = param ('phone');
$email = param ('email');

print qq(<div style="color:blue;font-size:3em;text-align:center;">); 
print "<p>Hello $first $last</p>";
print "<p>Your street name is $street</p>";
if (length($post) == 7 and $post =~ /[A-Z][0-9][A-Z]\s[0-9][A-Z][0-9]/ )
{
	 print "<p>$post is valid postal code\n</p>";
	
	
}
else{
	
	print "$post is not valid , please  go back and change\n";
}
print "<p>Your city name is $city and your province is $province</p>";

if (length($phone) == 10  and $phone =~  m/\d\d\d\d\d\d\d\d\d\d/ ) {
  print "<p>$phone is valid number\n</p>";
}
else{
	
	print "$phone is not valid , please  go back and change\n";
}
if($email =~ /^[a-z0-9A-Z][A-Za-z0-9.]+[A-Za-z0-9]\@[A-Za-z0-9.-]+$/)
{
	
	
	print "<p>$email is  valid email</p>";
}
else {
	print "<p>$email is not valid , please go back and change</p>";
	
}

print "</div>";