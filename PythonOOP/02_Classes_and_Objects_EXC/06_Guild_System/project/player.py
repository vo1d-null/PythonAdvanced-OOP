class Player:
    def __init__(self, name: str, hp: int, mp: int):
        # initializing the attributes of the player
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        # checking if the skill is already added
        if skill_name in self.skills.keys():
            return "Skill already added"
        # adding the skill to the player's collection
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        # creating a string to display the player's information
        result = f"Name: {self.name}\n"
        result += f"Guild: {self.guild}\n"
        result += f"HP: {self.hp}\nMP: {self.mp}\n"
        # displaying the player's skills
        for key, value in self.skills.items():
            result += f"==={key} - {value}\n"
        return result
