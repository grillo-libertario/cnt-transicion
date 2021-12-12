#!/bin/bash

# ConTeX
#pandoc -H context-header.tex -t context metadata.yaml */*md -s -o cnt-transicion.tex && context cnt-transicion.tex --result=cnt-transicion-context.pdf

echo compiling */*md

# LaTeX
pandoc --verbose -H header.tex -f markdown metadata.yaml  */*md -s -o cnt-transicion.pdf



