import turtle as t
import time
import snake  # imported just snake.py rather than from snake import Snake where Snake is the class name
import food
import scoreboard


screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# block1 = t.Turtle()
# block1.color("white")
# block1.shape("square")

screen.tracer(0)


snake1 = snake.Snake()  # here making an object named as sake1 just to make it more understandable and less confusing
# Now from snake we are initialising an object snake1 from the class named as Snake i.e. snake1 = snake.Snake()
food1 = food.Food()
scoreboard1 = scoreboard.Scoreboard()

screen.listen()
screen.onkey(fun=snake1.up, key="Up")
screen.onkey(fun=snake1.up, key="w")
screen.onkey(fun=snake1.down, key="Down")
screen.onkey(fun=snake1.down, key="s")
screen.onkey(fun=snake1.left, key="Left")
screen.onkey(fun=snake1.left, key="a")
screen.onkey(fun=snake1.right, key="Right")
screen.onkey(fun=snake1.right, key="d")

start_game = True

while start_game:
    screen.update()
    time.sleep(0.1)
    snake1.move()  # For our initialised object we are using move method from class Snake which is present in
    # snake.py file
    if snake1.head.distance(food1) < 15:
        food1.food_generation()
        snake1.extend()
        scoreboard1.score_incrementer()

    if snake1.head.xcor() > 289 or snake1.head.xcor() < -280 or snake1.head.ycor() > 288 or snake1.head.ycor() < -280:
        scoreboard1.reset()
        snake1.reset_snake()

    for segment in snake1.blocks[1:]:
        if snake1.head.distance(segment) < 10:
            scoreboard1.reset()
            snake1.reset_snake()

screen.exitonclick()
