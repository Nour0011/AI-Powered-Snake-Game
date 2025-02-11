from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        """Create a scoreboard to display the current score and high score."""
        super().__init__()
        self.score = 0
        with open("data") as data:
            self.high_score = int(data.read())  # Load the high score from a file
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update the scoreboard display."""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """Reset the current score and update the high score if necessary."""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data", mode="w") as data:
                data.write(f"{self.high_score}")  # Save the new high score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase the current score."""
        self.score += 1
        self.update_scoreboard()
