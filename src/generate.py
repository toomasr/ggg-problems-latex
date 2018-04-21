#!/usr/bin/python

import glob
import sys

if len(sys.argv) < 3:
    print "Usage: generate.py problem-folder output-tex-file"
    sys.exit(0)

problemFolder=sys.argv[1]
outputTexFile=sys.argv[2]

template = "src/templates/default.tex"
templateStr = ""
templateBlock = "src/templates/default-block.tex"
templateBlockStr = ""
templateBlockSingle = "src/templates/default-block.tex"
templateBlockSingleStr = ""

with open(template, "r") as myfile:
    templateStr = myfile.read()

with open(templateBlock, "r") as myfile:
    templateBlockStr = myfile.read()

with open(templateBlockSingle, "r") as myfile:
    templateBlockSingleStr = myfile.read()

images = glob.glob(problemFolder+"/*.png")
images.sort()

bodyResult = ""
counter = 0

for i in range(0, len(images), 2):
    image1 = images[i]
    image2 = images[i+1]
    if len(image1) > 0 and len(image2) > 0:
        bodyResult = bodyResult+templateBlockStr.replace("$PATH1",image1).replace("$PATH2", image2)+"\n"
    else:
        bodyResult = bodyResult+templateBlockSingleStr.replace("$PATH1",image1)+"\n"

    counter = counter + 1
    if counter % 3 == 0:
        counter = 0
        bodyResult = bodyResult + "\clearpage\n"

completeTexFile = templateStr.replace("$CONTENTS", bodyResult)

text_file = open(outputTexFile, "w")
text_file.write(completeTexFile)
text_file.close()
