from project.car import Car
class FamilyCar(Car):
    def __init__(self, fuel:float, horse_power:int):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION