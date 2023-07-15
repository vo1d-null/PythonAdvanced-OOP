from typing import List


class Smartphone:
    def __init__(self, memory: int):
        # Initialize the smartphone with given memory, empty app list, and turned off status
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def power(self) -> None:
        # Toggle the power status of the smartphone
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: int) -> str:
        # Check if the smartphone is turned on
        if not self.is_on:
            return f'Turn on your phone to install {app}'
        # Check if there is enough memory to install the app
        if self.memory > app_memory:
            # Deduct the app memory from the smartphone memory and add the app to the list
            self.memory -= app_memory
            self.apps.append(app)
            return f'Installing {app}'

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        # Get the total number of apps and memory left in the smartphone
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


# Create a new smartphone with 100 memory
smartphone = Smartphone(100)
# Try to install Facebook unmodified turning on the smartphone
print(smartphone.install("Facebook", 60))
# Turn on the smartphone and install Facebook, Messenger, and Instagram
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
# Check the status of the smartphone
print(smartphone.status())
