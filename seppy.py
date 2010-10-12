#!/usr/bin/python -tt
# Gary Doran, 2010

"""
A fun little Python program to generate a
self-enumerating pangram.
"""

import sys
import random
from string import ascii_lowercase

op = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
      "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"];

tp = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def generate(start):
    last_tallies = {}
    i = 0
    while True:
        sentence = make_sentence(start, last_tallies)
        tallies = tally(sentence)
        if last_tallies == tallies:
            break
        i += 1
        last_tallies = rand_tallies(last_tallies, tallies)
    return sentence

def rand_tallies(last_tallies, new_tallies):
    ret_val = {}
    diffs = tally_diffs(last_tallies, new_tallies)
    for c in ascii_lowercase:
        diff = diffs[c]
        if diff < 0:
            change = random.randint(diff, 0)
        else:
            change = random.randint(0, diff)
        count = 0
        if c in last_tallies:
            count = last_tallies[c]
        ret_val[c] = count + change
    return ret_val

def make_sentence(beginning, tallies):
    sentence = beginning
    for c in ascii_lowercase:
        count = 0
        if c in tallies:
            count = tallies[c]

        if c == 'z':
            sentence += 'and '
        sentence += number_to_word(count)
        sentence += ' ' + c
        if count != 1:
            sentence += "'s"
        if c != 'z':
            sentence += ', '
    sentence += '.'
    return sentence

def number_to_word(number):
    if number < 20:
        return op[number]
    elif number % 10 == 0:
        return tp[number / 10]
    else:
        return tp[number / 10] + '-' + op[number % 10]

def tally(sentence):
    tallies = {}
    for c in sentence.lower():
        if not c in ascii_lowercase:
            continue
        if c in tallies:
            tallies[c] = tallies[c] + 1
        else:
            tallies[c] = 1
    return tallies

def tally_diffs(old_tally, new_tally):
    diffs = {}
    for c in ascii_lowercase:
        old_c = 0
        if c in old_tally:
            old_c = old_tally[c]
        new_c = 0
        if c in new_tally:
            new_c = new_tally[c]
        diffs[c] = new_c - old_c
    return diffs

def main():
    if len(sys.argv) == 2:
        stub = sys.argv[1]
        if not stub[-1] == ' ':
            stub = stub + ' ';
        print generate(stub)
    else:
        print 'Please provide an argument that starts the pangram.'
        print '(For example: "Only a fool would check that this sentence contains")'

if __name__ == '__main__':
    main()
