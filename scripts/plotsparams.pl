#!/usr/bin/perl

# Plots S-parameters from a single exported CST file containing,
# e.g. S11, S21, and S22. A legend is shown on the output.

use warnings;
use strict;
use File::Basename;
use Getopt::Long;

sub printhelp {
    print "Usage:\n";
    print "    perl plotsparams.pl SPARAMETERFILE.txt OUTFILE.pdf\n";
    print "                        [-s|--show]        (show output file)\n";
    print "                        [-h|--help]        (show help message)\n";
    exit();
}

# Options and arguments
my $infile = "";
my $figurefile = "";
my $opt_showfigure = 0;
GetOptions(
    's|show' => \$opt_showfigure,
    'h|help' => sub { printhelp() }
);

# Input and output filenames are left in @ARGV.
if (not $ARGV[0]) {
    printhelp();
}
$infile = $ARGV[0];

open(my $infile_h, "<", $infile) or die "Could not open $infile. $!";

my $lines = join("", <$infile_h>);

my $p = qr{
    ^\s* Frequency 
    .*? (?:\s\s)+   # Column sep
    (.*?) /         # Run name
    .*? ^\s*-+\s*$  # Header sep line
    (.*?)           # Content
    ^\s*$           # Empty line => end
}xms;

my @outfiles = ();
my $paramname = "param";
while ($lines =~ /$p/g) {
    my $param = $1;
    my $rows = $2;

    $param =~ s/\s/_/g;
    $param =~ s/\(/[/g;
    $param =~ s/\)/]/g;
    $paramname = $param;
    $paramname = $1 if ($param =~ /^(.*?)=/);
    print "$param\n";

    my $outfile = "$param";
    open(my $outfile_h, ">", $outfile) or die "Could not open $outfile for writing";
    print $outfile_h "Frequency    $param\n$rows";
    close $outfile_h;
    push @outfiles, $outfile;
}

my $o = "sparams_$paramname.pdf";
if ($ARGV[1]) {
    $o = $ARGV[1];
}
my $here = dirname(__FILE__);
my $cmd = "python $here/plots11.py " . join(" ", @outfiles) . " -o $o";
$cmd .= " -s" if ($opt_showfigure);
system($cmd);

unlink $_ for @outfiles;
