#!/usr/bin/python -tt
# Gary Doran, 2010

"""
A fun little Python program to generate a
self-enumerating pangram.
"""

import sys

def main():
  if len(sys.argv) == 2:
    stub = sys.argv[1]
  else:
    print 'Please provide an argument that starts the pangram.'
    print '(For example: "Only a fool would check that this sentence contains")'

if __name__ == '__main__':
  main()
