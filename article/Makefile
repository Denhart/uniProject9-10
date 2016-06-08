all : pdf

LATEX             = pdflatex -shell-escape
BIBTEX            = bibtex

MAIN              = master
BIB               = bib/sources.bib
TEXFILES          = $(wildcard *.tex)\
		    $(wildcard set/*.tex)\
		    $(wildcard sec/*.tex)\
		    $(wildcard sec/*/*.tex)\
		    $(wildcard sec/*/*/*.tex)\
		    $(wildcard sec/*/*/*/*.tex)\
		    $(wildcard app/*.tex)\
		    $(wildcard tbl/*.tex)
IMAGES            = $(wildcard img/*)\
		    $(wildcard img/*/*)\
		    $(wildcard img/*/*/*)\
		    $(wildcard img/*/*/*/*)
EPSPDFFILES       = $(patsubst %.eps, %.pdf, $(wildcard img/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*/*.eps))
BILAG             = $(wildcard app/*/*.tex)

pdf : $(MAIN).pdf 

local : 
	$(LATEX) masterlocal.tex

force : 
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN).aux
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

$(MAIN).pdf :  $(TEXFILES) $(IMAGES)\
	$(EPSPDFFILES) $(BILAG) $(BIB)
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN).aux
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

clean :
	rm -f *.aux
	rm -f *.log
	rm -f *.bbl
	rm -f *.out
	rm -f *.bak
	rm -f *.blg
	rm -f *.toc
	rm -f *.lox
	rm -f *.auxlock
	rm -f *.fls
	rm -f *.upa
	rm -f *.upb
	rm -f *.lof
	rm -f *.fdb_latexmk
	rm -f img/*.bak

once : 
	$(LATEX) $(MAIN).tex

# EPS-FILES
%.pdf : %.eps
	epstopdf $*.eps

