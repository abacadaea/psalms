#!/bin/bash

import json
import re
import string

N = 4
filename = "psalms.json"
filename_out = "grams.%d.txt" % N
f = open(filename, "r")
h = json.load(f)
fout = open(filename_out,"w")
for verse in h:
    text = verse["text"] 
    text = text.split(':', 1)[-1]
    for char in "0123456789":
        text = text.replace(char, "")
    for char in string.punctuation:
        text = text.replace(char, " "+char)
    words = text.split()
    words.insert(0, "BEGIN_PSALM")
    words.append("END_PSALM")
    for i in range(len(words) - N + 1):
        for j in range(N-1):
            fout.write(words[i+j] + " ")
        fout.write(words[i + N - 1] + "\n")
