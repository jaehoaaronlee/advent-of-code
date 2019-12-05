#!/usr/bin/env ruby

require_relative 'intcode'

input = File.read('../input.txt')
codes = input.chomp.split(',').map(&:to_i)

expectation = 19690720

print "Figuring out"
(0..99).each do |noun|
  print "."
  (0..99).each do |verb|
    intcode = Intcode.new(codes).run(noun, verb)
    if intcode == expectation
      puts "\nnoun(#{noun}) * 100 + verb(#{verb}) = #{noun * 100 + verb}"
      exit
    end
  end
end
