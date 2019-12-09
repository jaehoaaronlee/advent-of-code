#!/usr/bin/env ruby

require_relative 'probe'

input = File.readlines("../input.txt")
paths = input.map { |line| line.chomp.split(',') }
probe = Probe.new(paths)
p "Closest: #{probe.closest_intersection} | Fewest: #{probe.fewest_steps}"
