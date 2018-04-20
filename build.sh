#!/bin/bash

# Delete old pdflatex files
rm build/*

# Generate the TeX file
echo "Outputting file to build/output.tex"
python src/generate.py
echo "/Outputting file to build/output.tex"

# Build the PDF
pdflatex -output-directory=build build/output.tex

# Move result to releases
cp build/output.pdf releases/
