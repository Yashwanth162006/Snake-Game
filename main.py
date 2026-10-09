from turtle import Turtle, Screen
import time

from food import Food
from snake import Snake
from scoreboard import Scoreboard

# Setup background screen
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('My Snake Game')
screen.tracer(0)

# Creating a snake
snake = Snake()

# Creating food
food = Food()

# Creating scoreboard
scoreboard = Scoreboard()

# Adding Event Listeners
screen.listen()
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.move()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if abs(snake.head.xcor())  > 380 or abs(snake.head.ycor()) > 280:
        scoreboard.game_over()
        game_on = False

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()