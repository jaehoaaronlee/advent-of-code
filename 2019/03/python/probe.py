from functools import reduce

class Probe:
  def __init__(self, paths):
    self.paths = paths
  
  def closest_intersection(self):
    return min(
      [
        sum([abs(intersection[0]), abs(intersection[1])])
          for intersection in self._intersections().keys()
      ]
    )

  def fewest_steps(self):
    return min(self._intersections().values())
  
  def _intersections(self):
    visited = []
    for instructions in self.paths:
      points = {}
      current = (0, 0)

      for instruction in instructions:
        direction, length = self._parse_instruction(instruction)
        steps = points.get(current, 0)

        for _ in range(length):
          current = self._take_instruction(current, direction)
          steps += 1

          if not points.get(current, None):
            points[current] = steps

      visited.append(points)

    intersections = set(list(visited[0].keys())) & set(list(visited[1].keys())) - set((0, 0))
    return {
      intersection: sum(p[intersection] for p in visited) \
      for intersection in intersections
    }

  def _take_instruction(self, origin, direction):
    return (origin[0] + direction[0], origin[1] + direction[1])
  
  def _parse_instruction(self, instruction):
    if instruction[0] == 'U':
      direction = [1, 0]
    elif instruction[0] == 'D':
      direction = [-1, 0]
    elif instruction[0] == 'L':
      direction = [0, -1]
    elif instruction[0] == 'R':
      direction = [0, 1]
  
    return [direction, int(instruction[1:])]