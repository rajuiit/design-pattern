# Old Media Players
class CassettePlayer:
    def play_cassette(self):
        return "Playing music from Cassette Player"

class CDPlayer:
    def play_cd(self):
        return "Playing music from CD Player"

# Adapter Class
class MediaAdapter:
    def __init__(self, media_device):
        self.media_device = media_device

    def play(self):
        if isinstance(self.media_device, CassettePlayer):
            return self.media_device.play_cassette()
        elif isinstance(self.media_device, CDPlayer):
            return self.media_device.play_cd()
        else:
            return "Unsupported media format"

# Modern Music System that only supports Bluetooth
class BluetoothMusicSystem:
    def __init__(self):
        self.connected_device = None

    def connect_device(self, adapter):
        self.connected_device = adapter

    def play_music(self):
        if self.connected_device:
            print("Music System Output: " + self.connected_device.play())
        else:
            print("No device connected.")

# Usage Example
if __name__ == "__main__":
    cassette = CassettePlayer()
    cd = CDPlayer()

    cassette_adapter = MediaAdapter(cassette)
    cd_adapter = MediaAdapter(cd)

    music_system = BluetoothMusicSystem()

    print("Connecting Cassette Player to Bluetooth System...")
    music_system.connect_device(cassette_adapter)
    music_system.play_music()

    print("\nConnecting CD Player to Bluetooth System...")
    music_system.connect_device(cd_adapter)
    music_system.play_music()
