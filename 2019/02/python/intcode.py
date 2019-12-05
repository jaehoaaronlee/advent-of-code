from typing import List

class Intcode:
  def __init__(self, codes: List[int]) -> None:
    self.codes = list(codes)

  def run(self, noun: int, verb: int) -> int:
    position = 0

    self.codes[1] = noun
    self.codes[2] = verb

    while self.codes[position] != 99:
      opcode = self.codes[position]
      lhs = self.codes[position + 1]
      rhs = self.codes[position + 2]
      res = self.codes[position + 3]

      if opcode == 1:
        self.codes[res] = self.codes[lhs] + self.codes[rhs]
      elif opcode == 2:
        self.codes[res] = self.codes[lhs] * self.codes[rhs]

      position += 4
      
    return self.codes[0]
