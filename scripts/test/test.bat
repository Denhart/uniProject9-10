rem Single S parameter
python ..\plots11.py singleS11.txt -o test1.pdf

rem Two single S parameters
python ..\plots11.py singleS11.txt singleS22.txt -o test2.pdf

rem Parameter sweep
perl ..\plotsweep.pl sweepS11.txt test3.pdf

rem Plot all S parameters (one file)
perl ..\plotsparams.pl allSparams.txt test4.pdf
