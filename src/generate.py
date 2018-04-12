#!/usr/bin/python

import glob

template = "src/templates/default.tex"
templateStr = ""
templateBlock = "src/templates/default-block.tex"
templateBlockStr = ""

with open(template, "r") as myfile:
	templateStr = myfile.read()

with open(templateBlock, "r") as myfile:
	templateBlockStr = myfile.read()

images = glob.glob("problems/*.png")
images.sort()

bodyResult = ""
counter = 0
for image in images:
	bodyResult = bodyResult+templateBlockStr.replace("$PATH", image)+"\n"
	counter = counter + 1
	if counter % 6 == 0:
		counter = 0
		bodyResult = bodyResult + "\clearpage\n"

completeTexFile = templateStr.replace("$CONTENTS", bodyResult)

text_file = open("build/output.tex", "w")
text_file.write(completeTexFile)
text_file.close()
