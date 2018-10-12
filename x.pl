#!perl
$A="browse.pyc";
open A or die "$A: $!";
read A, $b, 1024;               # Read up 1kb data from A file (PERL file handle) into $b (variable)
@c = unpack "C4A40(A/A)4", $b;  # Unpack data from $b into (map) variable @c using the provided unpacking template (the string parameter)

print "c=",@cs