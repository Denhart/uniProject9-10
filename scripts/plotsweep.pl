#!/usr/bin/perl
use warnings;
use strict;
use File::Basename;

if (not $ARGV[0]) {
    print "Usage:\n";
    print "    perl plotsweep.pl SWEEPFILE.txt OUTFILE.pdf\n"
}
my $infile = $ARGV[0];
open(my $infile_h, "<", $infile) or die "Could not open $infile. $!";

my $lines = join("", <$infile_h>);

my $p = qr{
   ^\s* Frequency
   .*? (\S+)/.*?
   ^-+$
   (.*?)
   ^$
}xms;

my @outfiles = ();
my $paramname = "param";
while ($lines =~ /$p/g) {
    my $param = $1;
    my $rows = $2;
    $paramname = $1 if ($param =~ /^(.*?)=/);

    my $outfile = "$param";
    open(my $outfile_h, ">", $outfile) or die "Could not open $outfile for writing";
    print $outfile_h "Frequency    $param\n$rows";
    close $outfile_h;
    push @outfiles, $outfile;
    print "$param\n";
}

my $o = "sweep_$paramname.pdf";
if ($ARGV[1]) {
    $o = $ARGV[1];
}
my $here = dirname(__FILE__);
my $cmd = "python $here/plots11.py " . join(" ", @outfiles) . " -n -o $o";
system($cmd);

unlink $_ for @outfiles;
