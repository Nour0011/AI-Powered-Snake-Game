from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from qlearning_agent import QLearningAgent
import time

# Set up the game screen
screen = Screen()
screen.setup(width=600, height=600)  # Define the game area dimensions
screen.bgcolor("black")  # Set the background color
screen.title("Snake Game with AI")  # Title of the game window
screen.tracer(0)  # Turn off automatic updates for smoother animations

# Initialize game components
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Define the possible actions the AI agent can take (Up, Down, Left, Right)
actions = [90, 270, 180, 0]  # Correspond to turtle headings
agent = QLearningAgent(actions)  # Create the Q-learning agent

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Refresh the game screen
    time.sleep(0.1)  # Slow down the game loop for better visibility
    state = (round(snake.head.xcor()), round(snake.head.ycor()))  # Current state of the agent

    # Let the agent decide the next action (exploration or exploitation)
    action_index = agent.choose_action(state)
    snake.set_heading(actions[action_index])  # Set the snake's direction
    snake.move()  # Move the snake in the chosen direction

    # Check for collisions with the food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move the food to a new random position
        snake.extend()  # Add a new segment to the snake
        scoreboard.increase_score()  # Increase the player's score
        agent.update_q_table(state, action_index, reward=10, next_state=state)  # Reward for eating food

    # Check for collisions with the wall
    if (
        snake.head.xcor() > 280 or snake.head.xcor() < -280 or
        snake.head.ycor() > 280 or snake.head.ycor() < -280
    ):
        scoreboard.reset()  # Reset the score and high score
        snake.reset()  # Reset the snake to its starting position
        agent.update_q_table(state, action_index, reward=-100, next_state=state)  # Negative reward for hitting a wall

    # Check for collisions with the snake's own body
    for segment in snake.segments[1:]:  # Skip the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()  # Reset the score
            snake.reset()  # Reset the snake
            agent.update_q_table(state, action_index, reward=-100, next_state=state)  # Negative reward for hitting itself

# Keep the game window open until clicked
# Save Q-table and exit
agent.save_q_table()
screen.exitonclick()
