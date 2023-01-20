#!/usr/bin/env python

import Factorial

if __name__ == '__main__':
  f = Factorial.Factorial()
  g = Factorial.Factorial(5)

  result_1 = f.compute()
  result_2 = g.compute()

  print "Factorial value 1: {}".format(result_1)
  print "Factorial value 2: {}".format(result_2)