#!/usr/bin/env python3

from password import Password

def apply_filter(code):
  password = Password(str(code))
  return password.is_valid()


if __name__ == '__main__':
  num_range = range(128392, 643282)
  num_combinations = len(list(filter(apply_filter, num_range)))
  print("There are {} combinations".format(num_combinations))
