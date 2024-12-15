import random
import time


class Pet:
    def __init__(self, name, hunger=0, happiness=0):
        self.name = name
        self.hunger = hunger
        self.happiness = happiness

    def feed(self):
        self.hunger -= 1
        print(f"{self.name} is happy, hunger reduced to {self.hunger}")

    def play(self):
        self.happiness += 1
        print(f"Playing made {self.name} happy, happiness increased to {self.hunger}")

    def status(self):
        print(f"{self.name}'s current hunger level: {self.hunger}")
        print(f"{self.name}'s current happiness level: {self.happiness}")


pet = Pet("Bobby")

while True:
    user_choice = input("> Talk to me: ")

    if user_choice == "feed":
        pet.feed()
    elif user_choice == "play":
        pet.play()
    elif user_choice == "status":
        pet.status()
    elif user_choice == "exit":
        break

    time.sleep(1)

print("Goodbye!")
