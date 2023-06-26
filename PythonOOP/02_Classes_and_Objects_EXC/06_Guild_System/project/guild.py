# Importing Player class from project.player module
from project.player import Player


# Defining Guild class
class Guild:
    # Constructor to initialize the name and players list
    def __init__(self, name: str):
        self.name = name
        self.players = []

    # Method to assign a player to the guild
    def assign_player(self, player: Player):
        # If player is already in the guild, return an appropriate message
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        # If player is in another guild, return an appropriate message
        if player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        # Assign the guild to the player and add the player to the guild's players list
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    # Method to kick a player from the guild
    def kick_player(self, player_name: str):
        # Iterate through the players list of the guild
        for player in self.players:
            # If the player is found, remove the player from the guild and set the guild to "Unaffiliated"
            if player.name == player_name:
                self.players.remove(player)
                player.guild = "Unaffiliated"
                return f"Player {player_name} has been removed from the guild."
        # If the player is not found, return an appropriate message
        return f"Player {player_name} is not in the guild."

    # Method to get the guild information
    def guild_info(self):
        # Initialize the result string with the guild name
        result = f"Guild: {self.name}\n"
        # Iterate through the players list of the guild and append the player information to the result string
        for player in self.players:
            result += f"{player.player_info()}\n"
        # Return the result string with any trailing whitespaces removed
        return result.strip()


# Create a new player object
player = Player("George", 50, 100)
# Add a new skill to the player and print the player information
print(player.add_skill("Shield Break", 20))
print(player.player_info())
# Create a new guild object
guild = Guild("UGT")
# Assign the player to the guild and print the guild information
print(guild.assign_player(player))
print(guild.guild_info())
