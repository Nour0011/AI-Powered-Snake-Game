from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        """Create a food object for the snake to eat."""
        super().__init__()
        self.shape("circle")  # Food is circular
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # Make the food smaller
        self.color("blue")
        self.speed("fastest")  # Make the food appear instantly
        self.refresh()

    def refresh(self):
        """Move the food to a new random location."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
