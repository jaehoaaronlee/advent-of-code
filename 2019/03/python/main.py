#!/usr/bin/env python3

from probe import Probe

def run():
  f = open('../input.txt', 'r')
  paths = [line.strip().split(',') for line in f.readlines()]
  f.close()
  probe = Probe(paths)
  print("Closest: {} | Fewest: {}".format(probe.closest_intersection(), probe.fewest_steps()))


if __name__ == '__main__':
  run()