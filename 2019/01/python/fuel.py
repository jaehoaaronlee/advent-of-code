class Fuel:
  @staticmethod
  def get_requirement(mass):
    return (mass // 3) - 2
    
  @staticmethod
  def get_recursive_requirement(mass):
    initial_fuel = Fuel.get_requirement(mass)

    if initial_fuel <= 0:
      return 0
    
    return initial_fuel + Fuel.get_recursive_requirement(initial_fuel)
