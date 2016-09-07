#!/bin/bash

FILENAME="enlacesEscuelas.txt"
while read line        
do  
    sleep 2      
    python getHtml.py -i "$line"
    python XMLsearch.py
    python XMLsearch2.py
    rm -r tempo.xml
done < $FILENAME

