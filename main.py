from turtle import Turtle, Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food
import time

BACKGROUND_COLOR = "blue"
GAME_TITLE = "My Snake Game"


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

segments = []

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.clear()
        scoreboard.goto(0, 270)
        scoreboard.inscrease_score()

    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
    
    for segment in snake.segments[1:]:
        if segment == snake.head:
            pass
        
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()



screen.exitonclick()