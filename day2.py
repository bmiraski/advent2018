"""Determine day 2 solution a for advent calendar."""

from collections import Counter

with open('inputday2.txt') as g:
    dataset = g.readlines()

double_letters = 0
triple_letters = 0

for line in dataset:
    lettercount = Counter(line)
    vals = lettercount.values()

    if 2 in vals:
        double_letters += 1
    if 3 in vals:
        triple_letters += 1

checksum = double_letters * triple_letters

print(checksum)
