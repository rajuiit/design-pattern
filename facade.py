class TV:
    def on(self):
        print("TV is now ON")

    def off(self):
        print("TV is now OFF")

    def set_channel(self, channel):
        print(f"TV is set to channel {channel}")

class SoundSystem:
    def on(self):
        print("Sound System is now ON")

    def set_volume(self, val):
        print(f"set_volume to {val}")

    def off(self):
        print(f"Sound System is now Off")

class Lights:
    def dim(self):
        print("Lights is now Dim")

    def bright(self):
        print("Lights is now bright")

class AirConditioner:
    def on(self):
        print("AirConditioner is now ON")

    def off(self):
        print("AirConditioner is now OFF")

    def set_temperature(self, temp):
        print(f"AirConditioner is set to temperature {temp}")

class SmartHomeFacade:
    def __init__(self):
        self.tv = TV()
        self.sound = SoundSystem()
        self.lights = Lights()
        self.ac = AirConditioner()

    def start_movie_night(self):
        print("\nStarting Movie Night Mode...")
        self.tv.on()
        self.tv.set_channel("Netflix")
        self.sound.on()
        self.sound.set_volume(20)
        self.lights.dim()
        self.ac.on()
        self.ac.set_temperature(22)
        print("Enjoy your movie! 🍿🎬\n")

    def shutdown(self):
        print("\nShutting down all systems...")
        self.tv.off()
        self.sound.off()
        self.lights.bright()
        self.ac.off()
        print("All devices are turned off. Goodbye!\n")

# Client code
obj = SmartHomeFacade()

obj.start_movie_night()
obj.shutdown()