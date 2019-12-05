#!/usr/bin/env ruby

require_relative 'fuel'

arguments = ARGF.argv
if arguments.length != 1
  p 'Wrong number of arguments. Only 1 permitted'
  return
elsif !['part1', 'part2'].include?(arguments.first.downcase)
  p 'Wrong argument. Permitted arguments: part1, part2'
  return
end

input = File.readlines('../input.txt')
amount = input.sum do |mass|
  case arguments.first.downcase
  when 'part1'
    Fuel.get_requirement(mass.to_i)
  when 'part2'
    Fuel.get_recursive_requirement(mass.to_i)
  end
end
p amount
