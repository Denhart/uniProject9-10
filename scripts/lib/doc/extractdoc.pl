use strict;
use warnings;
use Data::Dumper;

my $docpat = qr{
^ \s* $ \n       # Empty line
^ (\#.*?) $ \n   # Comment above function
^ def \s (.*?) : # Function name
}xms;

sub extractdoc {
    my $f = shift;
    open(my $f_h, "<", $f);
    my $l = join("", <$f_h>);
    close($f_h);

    my %doc = ();
    while ($l =~ /$docpat/g) {
        my $c = $1;
        my $f = $2;

        $f =~ s/_/\\_/xmsg;
        $c =~ s/^\#\s*$/<ENDDESC>/xms;
        $c =~ s/^\#\s//xmsg;
        $c =~ s/\@param \s+ (\w+)/- $1:/xmsg;
        $c =~ s/\@return\s+/\nReturn:\n/xmsg;
        $c =~ s/\@note\s+/\nNote:\n/xmsg;
        $c =~ s/^[ ]+/        /xmsg;

        $doc{$f} = $c;
    }

    return %doc;
}

sub layout {
    my $title = shift;
    my %hash = @_;
    my $format = "\\subsection{$title}\n";

    for my $f (sort keys %hash) {
        my $desc = "";
        my $doc = $hash{$f};
        ($desc,$doc) = ($1,$2) if ($hash{$f} =~ m/(.*?)<ENDDESC>\s*(.*)/xms);

        $format .= "\\subsubsection{$f}\n";
        $format .= "$desc\n\\begin{verbatim}\n$doc\n\\end{verbatim}\n\n";
    }
    return $format;
}

my %doc1 = extractdoc("../satimo.py");
my %doc2 = extractdoc("../cst.py");
my %doc3 = extractdoc("../l3d.py");

open(my $o_h, ">", "functiondoc.tex");
print $o_h layout("Satimo", %doc1);
print $o_h "\\clearpage\n";
print $o_h layout("CST", %doc2);
print $o_h "\\clearpage\n";
print $o_h layout("L3D", %doc3);
close($o_h);


