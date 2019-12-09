class Probe
  attr_reader :paths
  def initialize(paths)
    @paths = paths
  end

  def closest_intersection
    intersections.keys.map do |intersection|
      intersection.map(&:abs).sum
    end.min
  end

  def fewest_steps
    intersections.values.min
  end

  private

  def intersections
    visited =
      @paths.map do |instructions|
        points = {}
        current = [0, 0]

        instructions.each do |instruction|
          direction, length = parse_instruction(instruction)
          steps = points[current] || 0

          length.times do
            current = take_instruction(current, direction)
            steps += 1

            points[current] ||= steps
          end
        end

        points
      end

    intersections = visited.map(&:keys).reduce(:&)
    intersections.map do |intersection|
      [intersection, visited.sum { |point| point[intersection] }]
    end.to_h
  end

  def take_instruction(origin, direction)
    [origin[0] + direction[0], origin[1] + direction[1]]
  end

  def parse_instruction(instruction)
    direction =
      case instruction[0]
      when 'U'
        [1, 0]
      when 'D'
        [-1, 0]
      when 'L'
        [0, -1]
      when 'R'
        [0, 1]
      end

    length = instruction[1..-1].to_i

    [direction, length]
  end
end
