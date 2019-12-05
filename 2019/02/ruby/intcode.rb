class Intcode
  attr_reader :codes

  def initialize(codes)
    @codes = codes.dup
  end

  def run(noun, verb)
    codes[1] = noun
    codes[2] = verb

    position = 0

    while codes[position] != 99
      opcode = codes[position]
      position_lhs = codes[position + 1]
      position_rhs = codes[position + 2]
      position_result = codes[position + 3]

      case opcode
      when 1
        codes[position_result] = codes[position_lhs] + codes[position_rhs]
      when 2
        codes[position_result] = codes[position_lhs] * codes[position_rhs]
      end

      position += 4
    end

    codes[0]
  end
end
