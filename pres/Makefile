all : pdf

pdf : $(wildcard *.tex) $(wildcard sec/*.tex) $(wildcard img/*.tex)
	pdflatex pres.tex
	pdflatex pres.tex

force : 
	pdflatex pres.tex
	pdflatex pres.tex

once : 
	pdflatex pres.tex

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
	rm -f *.nav
	rm -f *.snm
	rm -f *.vrb
	rm -f *.fdb_latexmk
	rm -f img/*.bak
