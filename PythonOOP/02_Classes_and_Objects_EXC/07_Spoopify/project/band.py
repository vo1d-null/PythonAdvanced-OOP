from project.album import Album


class Band:
    def __init__(self, name: str):
        # initialize band with name and empty list of albums
        self.name = name
        self.albums = []

    def add_album(self, album: Album):
        # if album is already in the list, return message
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        # if album is not in the list, add it and return message
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        # check if album is in the list, if yes, remove it and return message
        for album in self.albums:
            if album.name == album_name:
                if album.published:
                    return "Album has been published. It cannot be removed."
                self.albums.remove(album)
                return f"Album {album.name} has been removed."
        # if album is not in the list, return message
        return f"Album {album_name} is not found."

    def details(self):
        # create result string with band name and album details
        result = f"Band {self.name}\n"
        for album in self.albums:
            result += f"{album.details()}\n"
        # return result string without trailing newline
        return result.strip()
