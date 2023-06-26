# This class represents a song
class Song:
    # Constructor to initialize the song object
    def __init__(self, name: str, length: float, single: bool):
        self.name = name
        self.length = length
        self.single = single

    # Method to get information about the song
    def get_info(self):
        return f"{self.name} - {self.length}"
