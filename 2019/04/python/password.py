from collections import Counter

class Password:
  def __init__(self, code: int) -> None:
    self.code = code

  def is_valid(self) -> bool:
    if self._has_double() and self._is_increasing() and self._has_group_of_two():
      return True
    return False

  def _has_double(self) -> bool:
    for char_1, char_2 in zip(self.code, self.code[1:]):
      if char_1 == char_2:
        return True

    return False

  def _is_increasing(self) -> bool:
    for char_1, char_2 in zip(self.code, self.code[1:]):
      if char_1 > char_2:
        return False

    return True

  def _has_group_of_two(self) -> bool:
    counts = Counter(self.code)
    for count in counts.values():
      if count == 2:
        return True

    return False
