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

images = glob.glob("problems/easy/*.png")
images.sort()

bodyResult = ""
counter = 0

for i in range(0, len(images), 2):
    image1 = images[i]
    image2 = images[i+1]
    bodyResult = bodyResult+templateBlockStr.replace("$PATH1",image1).replace("$PATH2", image2)+"\n"

    counter = counter + 1
    if counter % 3 == 0:
        counter = 0
        bodyResult = bodyResult + "\clearpage\n"

completeTexFile = templateStr.replace("$CONTENTS", bodyResult)

text_file = open("build/output.tex", "w")
text_file.write(completeTexFile)
text_file.close()
