class Animal:
    def __init__(self, name, energy):
        self.name = name
        self.energy = energy

    def eat(self, energy_gain):
        self.energy += energy_gain
        print(f"{self.name} is eating and gained {energy_gain} energy. His energy is now {self.energy}")

    def sleep(self, energy_gain):
        self.energy += energy_gain
        print(f"{self.name} is sleeping and gained {energy_gain} energy. His energy is now {self.energy}")

    def play(self, energy_loss):
        self.energy -= energy_loss
        print(f"{self.name} is playing and lost {energy_loss} energy. His energy is now {self.energy}")


