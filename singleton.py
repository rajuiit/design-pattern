class SmartHomeConfigManager:
    _instance = None  

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SmartHomeConfigManager, cls).__new__(cls, *args, **kwargs)
            cls._instance.settings = {}
        return cls._instance

    def set_setting(self, key, value):
        self.settings[key] = value

    def get_setting(self, key):
        return self.settings.get(key, None)
    
    
class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.config = SmartHomeConfigManager()

    def display_settings(self):
        print(f"[{self.name}] Current Settings: {self.config.settings}")

    def update_setting(self, key, value):
        print(f"[{self.name}] Updating {key} to {value}")
        self.config.set_setting(key, value)



if __name__ == "__main__":
    # Retrieve the Singleton instance
    config_manager = SmartHomeConfigManager()

    # Set initial configuration
    config_manager.set_setting("temperature", 22)
    config_manager.set_setting("lights", "dim")

    # Create smart devices
    device1 = SmartDevice("Thermostat")
    device2 = SmartDevice("Living Room Lights")

    # Display shared settings
    device1.display_settings()
    device2.display_settings()

    # Update settings from one device
    device1.update_setting("temperature", 24)

    # Display updated settings
    device1.display_settings()
    device2.display_settings()
