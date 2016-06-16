#!/bin/zsh
cd corrside
splitsweep.pl $(ls *.txt)
cd ..

cd corrtop
splitsweep.pl $(ls *.txt)
cd ..

cd s11top
splitsweep.pl $(ls *.txt)
cd ..

cd s21top
splitsweep.pl $(ls *.txt)
cd ..

cd s21side
splitsweep.pl $(ls *.txt)
cd ..

cd s22side
splitsweep.pl $(ls *.txt)
cd ..
