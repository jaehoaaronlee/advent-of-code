#!/usr/bin/env python

from fuel import Fuel
from sys import argv, exit

def run(test_case):
  f = open('../input.txt', 'r')
  sum = 0
  
  for line in f:
    mass = int(line)
    if test_case == 'part1':
      sum += Fuel.get_requirement(mass)
    else:
      sum += Fuel.get_recursive_requirement(mass)
  
  return sum

if __name__ == '__main__':
  if len(argv) != 2:
    exit('Wrong number of arguments: required 1')
  elif argv[1].lower() not in ['part1', 'part2']:
    exit('Wrong argument. Accepted: [part1, part2]')

  print(run(argv[1].lower()))