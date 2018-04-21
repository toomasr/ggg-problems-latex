#!/bin/bash

# Delete old pdflatex files
rm build/*

# Generate the TeX file
python src/generate.py problems/easy/ build/easy.tex
python src/generate.py problems/intermediate/ build/intermediate.tex
python src/generate.py problems/hard/ build/hard.tex

# Build the PDF
pdflatex -output-directory=build build/easy.tex
pdflatex -output-directory=build build/intermediate.tex
pdflatex -output-directory=build build/hard.tex

# Move result to releases
if [[ "$@" == "release" ]];then
  cp build/easy.pdf releases/easy-problems.pdf
  cp build/intermediate.pdf releases/intermediate-problems.pdf
  cp build/hard.pdf releases/hard-problems.pdf
fi
