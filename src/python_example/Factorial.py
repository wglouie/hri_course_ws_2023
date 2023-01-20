#!/usr/bin/env python

class Factorial:
  def __init__(self,n=3):
    self.n = n

  def compute(self):
    result = 1
    for i in range(1,self.n+1):
      result = result * i
    
    return result