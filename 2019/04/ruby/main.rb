#!/usr/bin/env ruby

require_relative 'password'

range = (128392..643281)
num_combinations = range.select do |code|
  Password.new(code).valid?
end.count
p "There are #{num_combinations} combinations."