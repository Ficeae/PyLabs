from SpecifiedHomeAppliances import *

app = HomeAppliance("Vacuum", False, 3.3, 2000)
washer = Washer("Samsung UberWasherMachine8000", True, 2.8, 2011, 2200, 30)
vacuum_cleaner = VacuumCleaner("Philips VC4", False, 1.2, 2019, 4)
tv = TV("LG WideEnough", True, 1, 2019, 77.7)
tape_recorder = TapeRecorder("TheTapes 90", False, 0.3, 1990, False)
radio = Radio("Mein RAA DI O", False, 0.5, 2019, 111.6)
music_center = MusicCenter("Sony HomeOrchestra", True, 4, 2021, "DOBROHO VECHORA")

print(app, washer, vacuum_cleaner, tv, tape_recorder, radio, music_center)
music_center.play_song()
