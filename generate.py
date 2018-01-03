#!/bin/bash

import json
import random
import re
import string

N = 7
filename_in = "grams.%d.txt" % N
filename_out = "psalms.%d.txt" % N
fin = open(filename_in, "r")
fout = open(filename_out, "w")

def sample(d):
    r = random.random() * d["NUM"]
    s = 0.0
    for key in d:
        if key == "NUM":
            continue
        s += d[key]
        if r < s:
            return key
    assert(False)

seeds = []

lookup = {}
for line in fin.readlines():
    words = line.split()
    if words[0] == "BEGIN_PSALM":
        seeds.append(words)
        continue
    assert(len(words) == N)
    tup = tuple(words[:-1])
    if tup not in lookup:
       lookup[tup] = {"NUM": 0}
    lookup[tup]["NUM"] += 1
    if words[-1] not in lookup[tup]:
        lookup[tup][words[-1]] = 0
    lookup[tup][words[-1]] += 1

for i in range(100):
    sentence = random.choice(seeds)
    while sentence[-1] != "END_PSALM":
        tup = tuple(sentence[-(N-1):])
        next_word = sample(lookup[tup])
        sentence.append(next_word)
    fout.write(' '.join(sentence) + '\n')
