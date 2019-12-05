#!/usr/bin/env python3

from intcode import Intcode
from sys import exit

def run() -> str:
  f = open('../input.txt', 'r')
  codes = [int(code) for code in f.read().strip().split(',')]
  f.close()

  expectation = 19690720
  
  print("Calculating", end = "")
  for noun in range(100):
    print(".", end = "")
    for verb in range(100):
      intcode = Intcode(codes)
      result = intcode.run(noun, verb)
      if result == expectation:
        return "\nnoun({}) * 100 + verb({}) = {}".format(noun, verb, noun * 100 + verb)

if __name__ == "__main__":
  print(run())