from turtle import Turtle

# Constants for the snake's behavior
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions of the snake segments
MOVE_DISTANCE = 20  # Distance the snake moves in one step

class Snake:
    def __init__(self):
        """Initialize the snake with three segments."""
        self.segments = []  # List of turtle objects representing the snake
        self.create_snake()  # Create the initial snake body
        self.head = self.segments[0]  # The first segment is the head of the snake

    def create_snake(self):
        """Create the initial snake with three segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a segment to the snake at a given position."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()  # Prevent the snake from drawing on the screen
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset(self):
        """Reset the snake to its starting position."""
        for seg in self.segments:
            seg.goto(1000, 1000)  # Move all segments off-screen
        self.segments.clear()  # Clear the segments list
        self.create_snake()  # Recreate the snake
        self.head = self.segments[0]

    def extend(self):
        """Add a new segment to the snake."""
        self.add_segment(self.segments[-1].position())  # Add the segment at the tail

    def set_heading(self, heading):
        """Set the direction of the snake's head."""
        self.head.setheading(heading)

    def move(self):
        """Move the snake forward."""
        # Move each segment to the position of the segment ahead of it
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)  # Move the head forward
