all : pdf

LATEX             = pdflatex -shell-escape -file-line-error
BIBTEX            = bibtex
LATEXMK           = latexmk -shell-escape -pdf

MAIN              = master
MAINKINDLE        = masterkindle
BIB               = bib/sources.bib
TEXFILES          = $(wildcard *.tex)\
		    $(wildcard set/*.tex)\
                    $(wildcard sec/*.tex)\
		    $(wildcard sec/*/*.tex)\
		    $(wildcard sec/*/*/*.tex)\
		    $(wildcard sec/*/*/*/*.tex)\
		    $(wildcard app/*.tex)\
		    $(wildcard app/*/*.tex)\
		    $(wildcard app/*/*/*.tex)\
		    $(wildcard app/*/*/*/*.tex)\
		    $(wildcard tbl/*.tex)
IMAGES            = $(wildcard img/*)\
		    $(wildcard img/*/*)\
		    $(wildcard img/*/*/*)\
		    $(wildcard img/*/*/*/*)\
		    $(wildcard img/*/*/*/*/*)\
		    $(wildcard img/*/*/*/*/*/*)\
		    $(wildcard img/*/*/*/*/*/*/*)\
		    $(wildcard img/*/*/*/*/*/*/*/*)
EPSPDFFILES       = $(patsubst %.eps, %.pdf, $(wildcard img/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*/*/*/*.eps))\
		    $(patsubst %.eps, %.pdf, $(wildcard img/*/*/*/*/*/*/*/*.eps))
BILAG             = $(wildcard app/*/*.tex)

pdf : $(MAIN).pdf 

local : 
	$(LATEX) masterlocal.tex

force : 
	$(LATEXMK) $(MAIN)

$(MAIN).pdf :  $(TEXFILES) $(IMAGES) $(EPSPDFFILES) $(BILAG) $(BIB)
	$(LATEXMK) $(MAIN)

kindle : $(TEXFILES) $(IMAGES) $(EPSPDFFILES) $(BILAG) $(BIB)
	cp $(MAIN).tex $(MAINKINDLE).tex
	perl -i'' -p -e 's/set\/preamble/set\/preamblekindle/' $(MAINKINDLE).tex
	$(LATEXMK) $(MAINKINDLE)	

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
	rm -f img/tikztmp/*

once : 
	$(LATEX) $(MAIN).tex

love :
	@echo "not war"

# EPS-FILES
%.pdf : %.eps
	epstopdf $*.eps
