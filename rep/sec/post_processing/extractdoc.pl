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
    # my $format = "\\subsubsection{$title}\n";
    my $format = "";

    for my $f (sort keys %hash) {
        my $desc = "";
        my $doc = $hash{$f};
        ($desc,$doc) = ($1,$2) if ($hash{$f} =~ m/(.*?)<ENDDESC>\s*(.*)/xms);
        $desc =~ s/_/\\_/g;
        $desc =~ s/"(\w)/``$1/g;
        $desc =~ s/(\w)"/$1''/g;

        $format .= "\\subsubsection{$f}\n";
        $format .= "$desc\n\\begin{lstlisting}[numbers=none, frame=none, xleftmargin=0em, language=, basicstyle=\\footnotesize\\ttfamily]\n$doc\n\\end{lstlisting}\n\n";
    }
    return $format;
}

my %doc1 = extractdoc("../../../scripts/lib/satimo.py");
my %doc2 = extractdoc("../../../scripts/lib/cst.py");
my %doc3 = extractdoc("../../../scripts/lib/l3d.py");
my %doc4 = extractdoc("../../../scripts/lib/aauplot.py");
my $o_h;

open($o_h, ">", "functiondoc_satimo.tex");
print $o_h layout("Satimo", %doc1);
close($o_h);

open($o_h, ">", "functiondoc_cst.tex");
print $o_h layout("CST", %doc2);
close($o_h);

open($o_h, ">", "functiondoc_l3d.tex");
print $o_h layout("L3D", %doc3);
close($o_h);

open($o_h, ">", "functiondoc_aauplot.tex");
print $o_h layout("AAUplot", %doc4);
close($o_h);
