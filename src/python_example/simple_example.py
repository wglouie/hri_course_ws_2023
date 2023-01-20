#!/usr/bin/env python

import sys

if __name__ == '__main__':
  n = len(sys.argv)
  print "Total arguments: {}".format(n)

  print "\n Name of the Python script: {}".format(sys.argv[0])

  print("\nArguements passed:")
  for i in range(1,n):
    print(sys.argv[i])
  
  sum = 0

  for i in range(1,n):
    sum += int(sys.argv[i])
  
  print "\nResult: {}".format(sum)
