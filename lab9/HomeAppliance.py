class HomeAppliance:
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int):
        self.model = model
        self.is_on = is_on
        self.kwh_per_hour = kwh_per_hour
        self.year_of_production = year_of_production

    def __str__(self):
        return f"_______________________________\n" \
               f"|Home appliance\n" \
               f"|- Model: {self.model}\n" \
               f"|- Is ON: {self.is_on}\n" \
               f"|- Electricity consumption: {self.kwh_per_hour} kWh per hour\n" \
               f"|- Year of production: {self.year_of_production}\n"
