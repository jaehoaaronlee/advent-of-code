class Password
  attr_reader :code

  def initialize(code)
    @code = code.to_s
  end

  def valid?
    has_double && !decreasing && group_of_two?
  end

  private

  def zipped
    chars = code.chars
    chars[1...chars.length].zip(chars)
  end

  def has_double
    zipped.any? do |char_1, char_2|
      char_1 == char_2
    end
  end

  def decreasing
    zipped.any? do |char_1, char_2|
      char_1 < char_2
    end
  end

  def group_of_two?
    counter = {}
    code.chars.each do |char|
      counter[char] = (counter[char] || 0) + 1
    end

    counter.values.any? { |key| key == 2 }
  end
end
