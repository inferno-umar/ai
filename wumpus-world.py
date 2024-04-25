"""
Implement Wumpus World

Experiment: 5

@Learner: TE-CO
Name: Arman Aslam Khan
Roll No: 22DCO03
Batch: 3
Academic Year: 2024
Sem - 6
"""

# Program:

import random

class WumpusWorld:
    def __init__(self, size=4):
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
        self.wumpus_location = (random.randint(0, size-1), random.randint(0, size-1))
        self.gold_location = (random.randint(0, size-1), random.randint(0, size-1))
        while self.gold_location == self.wumpus_location:
            self.gold_location = (random.randint(0, size-1), random.randint(0, size-1))
        self.pit_locations = []
        self.agent_location = (0, 0)
        self.generate_pits()

    def generate_pits(self):
        num_pits = min(self.size, 3)
        for _ in range(num_pits):
            pit_location = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            while pit_location == self.agent_location or pit_location == self.wumpus_location or pit_location == self.gold_location or pit_location in self.pit_locations:
                pit_location = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            self.pit_locations.append(pit_location)

    def display(self):
        for i in range(self.size):
            print('+---'*self.size + '+')
            for j in range(self.size):
                if (i, j) == self.agent_location:
                    print('| A ', end='')
                elif (i, j) == self.wumpus_location:
                    print('| W ', end='')
                elif (i, j) == self.gold_location:
                    print('| G ', end='')
                elif (i, j) in self.pit_locations:
                    print('| P ', end='')
                else:
                    print('|   ', end='')
            print('|')
        print('+---'*self.size + '+')

    def move_agent(self, direction):
        x, y = self.agent_location
        if direction == 'up' and x > 0:
            self.agent_location = (x-1, y)
        elif direction == 'down' and x < self.size-1:
            self.agent_location = (x+1, y)
        elif direction == 'left' and y > 0:
            self.agent_location = (x, y-1)
        elif direction == 'right' and y < self.size-1:
            self.agent_location = (x, y+1)
        else:
            print("Invalid move! Try again.")

    def check_game_over(self):
        if self.agent_location == self.wumpus_location:
            print("Game over! You were eaten by the Wumpus.")
            return True
        elif self.agent_location == self.gold_location:
            print("Congratulations! You found the gold.")
            return True
        elif self.agent_location in self.pit_locations:
            print("Game over! You fell into a pit.")
            return True
        else:
            return False

if __name__ == "__main__":
    world = WumpusWorld()
    print("Welcome to Wumpus World!")
    while True:
        world.display()
        action = input("Enter your move (up/down/left/right): ").lower()
        world.move_agent(action)
        if world.check_game_over():
            break

'''
Output:
PS C:\Users\Desktop\22DCO03> python woum.py
Welcome to Wumpus World!
+---+---+---+---+
| A |   |   | W |
+---+---+---+---+
| P |   |   |   |
+---+---+---+---+
|   |   | P |   |
+---+---+---+---+
|   | G |   | P |
+---+---+---+---+
Enter your move (up/down/left/right): up
Invalid move! Try again.
+---+---+---+---+
| A |   |   | W |
+---+---+---+---+
| P |   |   |   |
+---+---+---+---+
|   |   | P |   |
+---+---+---+---+
|   | G |   | P |
+---+---+---+---+
Enter your move (up/down/left/right): down
Game over! You fell into a pit.
'''

