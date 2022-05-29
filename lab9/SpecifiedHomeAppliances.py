from HomeAppliance import *


class Washer(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int, rpm: int,
                 capacity_in_liters: int):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.rpm = rpm
        self.capacity_in_liters = capacity_in_liters

    def __str__(self):
        return super(Washer, self).__str__() + f"|- RPM: {self.rpm}\n" \
                                               f"|- Capacity (liters): {self.capacity_in_liters}\n"


class VacuumCleaner(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int, nozzles_amount: int):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.nozzles_amount = nozzles_amount

    def __str__(self):
        return super(VacuumCleaner, self).__str__() + f"|- Nozzles amount: {self.nozzles_amount}\n"


class TV(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int,
                 screen_size_inches: float):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.screen_size_inches = screen_size_inches

    def __str__(self):
        return super(TV, self).__str__() + f"|- Screen size: {self.screen_size_inches}``\n"


class TapeRecorder(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int, is_tape_set: bool):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.is_tape_set = is_tape_set

    def __str__(self):
        return super(TapeRecorder, self).__str__() + f"|- Is tape inside: {self.is_tape_set}\n"


class Radio(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int, frequency: float):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.frequency = frequency

    def __str__(self):
        return super(Radio, self).__str__() + f"|- Current frequency: {self.frequency}\n"


class MusicCenter(HomeAppliance):
    def __init__(self, model: str, is_on: bool, kwh_per_hour: float, year_of_production: int, current_song: str):
        super().__init__(model, is_on, kwh_per_hour, year_of_production)
        self.current_song = current_song

    def play_song(self):
        if self.is_on:
            print("Now playing: ", self.current_song)
        else:
            print("Music center is OFF")

    def __str__(self):
        return super(MusicCenter, self).__str__() + f"|- Current song in list: {self.current_song}\n"
