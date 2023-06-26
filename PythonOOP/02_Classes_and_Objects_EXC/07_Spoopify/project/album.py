from project.song import Song


class Album:
    def __init__(self, name: str, *songs):
        # initialize album name, songs list and published status
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song: Song):
        # check if song is a single
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        # check if album is already published
        if self.published:
            return "Cannot add songs. Album is published."
        # check if song is already in album
        if song in self.songs:
            return "Song is already in the album."
        # add song to album if it passes all checks
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        # check if album is already published
        if self.published:
            return "Cannot remove songs. Album is published."
        # iterate through songs in album and remove song if found
        for song in self.songs:
            if song.name == song_name:
                self.songs.remove(song)
                return f"Removed song {song_name} from album {self.name}."
        # if song not found in album
        return "Song is not in the album."

    def publish(self):
        # check if album is already published
        if self.published:
            return f"Album {self.name} is already published."
        # publish album if it passes check
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        # initialize album details string
        result = f"Album {self.name}\n"
        # iterate through songs in album and add their details to the result string
        for song in self.songs:
            result += f"== {song.get_info()}\n"
        # return the result string with leading/trailing whitespace removed
        return result.strip()
