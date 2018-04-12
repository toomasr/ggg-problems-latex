#!/bin/bash

# Generate the TeX file

python src/generate.py

# Build the PDF

pdflatex -output-directory=build build/output.tex 
