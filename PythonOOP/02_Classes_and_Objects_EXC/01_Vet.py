from typing import List


class Vet:
    # List of animals in the clinic
    animals: List[str] = []
    # Maximum space in the clinic
    space = 5

    def __init__(self, name: str):
        # Vet's name
        self.name = name
        # List of animals registered by the vet
        self.animals: List[str] = []

    def register_animal(self, animal: str):
        # Check if there is enough space in the clinic
        if len(self.animals) >= Vet.space:
            return "Not enough space"
        # Add the animal to the vet's list and the clinic's list
        self.animals.append(animal)
        Vet.animals.append(animal)
        return f"{animal} registered in the clinic"

    def unregister_animal(self, animal: str):
        # Check if the animal is registered with the vet
        if animal not in self.animals:
            return f"{animal} not in the clinic"
        # Remove the animal from the vet's list and the clinic's list
        self.animals.remove(animal)
        Vet.animals.remove(animal)
        return f"{animal} unregistered successfully"

    def info(self):
        # Calculate the space left in the clinic
        space_left = abs(len(Vet.animals) - Vet.space)
        return f"{self.name} has {len(self.animals)} animals. {space_left} space left in clinic"


# Create two vets
peter = Vet("Peter")
george = Vet("George")
# Register and unregister animals with the vets
print(peter.register_animal("Tom"))
print(george.register_animal("Cory"))
print(peter.register_animal("Fishy"))
print(peter.register_animal("Bobby"))
print(george.register_animal("Kay"))
print(george.unregister_animal("Cory"))
print(peter.register_animal("Silky"))
print(peter.unregister_animal("Molly"))
print(peter.unregister_animal("Tom"))
# Get info about the vets
print(peter.info())
print(george.info())
