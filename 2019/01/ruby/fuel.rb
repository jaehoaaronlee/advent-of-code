module Fuel
  class << self
    def get_requirement(mass)
      (mass / 3) - 2
    end

    def get_recursive_requirement(mass)
      initial_fuel = get_requirement(mass)
      return 0 if initial_fuel <= 0

      initial_fuel + get_recursive_requirement(initial_fuel)
    end
  end
end
