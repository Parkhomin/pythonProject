class Car:
    model = None
    year = None
    engine = None

    def __init__(self, model, year, engine):
        self.model = model
        self.year = year
        self.engine = engine

    def present(self):
        print(" | " + self.model + " | " + self.year + " | " + self.engine + " | ")


class OilVolume:
    oil = None
    gas = None
    transmission = None

    def __init__(self, oil, gas, transmission):
        self.oil = oil
        self.gas = gas
        self.transmission = transmission

    def gasoline(self):
        print(" " * 25 + " / " + self.oil + " / " + self.gas + " / " + self.transmission + " / ")


number1 = Car("RAV4", "2012", "2.4")
number2 = Car("A65R35", "2021", "2,8 ISF")

tank1 = OilVolume("5w30", "petrol", "ATF")
tank2 = OilVolume("5w40", "diesel", "75w90")

number1.present(), tank1.gasoline(), print("-" * 25)
number2.present(), tank2.gasoline(), print("-" * 25)