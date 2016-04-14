all : pdf

LATEX             = pdflatex -shell-escape -file-line-error
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
	$(LATEX) $(MAIN).tex
	$(BIBTEX) $(MAIN).aux
	$(LATEX) $(MAIN).tex
	$(LATEX) $(MAIN).tex

$(MAIN).pdf :  $(TEXFILES) $(IMAGES) $(EPSPDFFILES) $(BILAG) $(BIB)
	latexmk -pdf $(MAIN)

	# @ echo "*** RUNNING LATEX FIRST TIME ***"
	# @ $(LATEX) $(MAIN).tex
	# @ if egrep -s 'No file.*\.bbl|Citation.*?undefined' $(MAIN).log;then\
	# 	echo "*** RUNNING BIBTEX AND LATEX ***" ;\
	# 	$(BIBTEX) $(MAIN).aux ;\
	# 	$(LATEX) $(MAIN).tex ;\
	# 	fi
	# @ if egrep -s 'No file.*\.bbl|Citation.*?undefined' $(MAIN).log;then\
	# 	echo "*** RUNNING BIBTEX AND LATEX AGAIN ***" ;\
	# 	$(BIBTEX) $(MAIN).aux ;\
	# 	$(LATEX) $(MAIN).tex ;\
	# 	fi
	# @ if egrep -s 'Rerun (LaTeX|to get cross-references right)' $(MAIN).log;then\
	# 	echo "*** RUNNING LATEX AGAING TO GET REFERENCES ***" ;\
	# 	$(LATEX) $(MAIN).tex ;\
	# 	fi

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
