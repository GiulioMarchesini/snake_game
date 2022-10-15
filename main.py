from turtle import Screen, Turtle
import random
import time
from scoreboard import Scoreboard


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#screen setup
screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
pulsanti= ["Right","Up","Left","Down"]
snake=0
food=0
scoreboard=0

class Snake:
    def __init__(self):
        self.snake_body=[]
        self.create_snake()
        self.snake_head= self.snake_body[0]
        self.direction= pulsanti[0]

    def create_snake(self):
        for i in range(3):
            new_part=Turtle("square")
            new_part.color("white")
            new_part.up()
            new_part.goto(x=-20*i,y=0)
            new_part.speed("fastest")
            self.snake_body.append(new_part)
        screen.update()

    def move(self):
        for i in range(len(self.snake_body)-1,0,-1):
            new_x=self.snake_body[i-1].xcor()
            new_y=self.snake_body[i-1].ycor()
            self.snake_body[i].goto(new_x,new_y)
        self.snake_head.forward(20)
        screen.update()
    
    def key_pressed(self,key):
        if self.direction == "Right" or self.direction== "Left":
            if key== "Up":
                self.snake_head.setheading(90)
                self.direction="Up"
            elif key== "Down":
                self.snake_head.seth(270)
                self.direction="Down"
        elif self.direction == "Up" or self.direction== "Down":
            if key== "Right":
                self.snake_head.seth(0)
                self.direction="Right"
            elif key== "Left":
                self.snake_head.seth(180)
                self.direction="Left"
        # screen.update()
        self.move()

    def increase_size(self):    
        #increase size of snake
        new_part = Turtle("square")
        new_part.color("white")
        new_part.up()
        #control the position of the last part of the snake
        new_part.goto(x=self.snake_body[-1].xcor() - 20, y=self.snake_body[-1].ycor())
        self.snake_body.append(new_part)
        screen.update()

def game_setup():
    global snake
    global food
    global scoreboard
    scoreboard = Scoreboard()
    snake= Snake()

    #set up the key bindings
    for i in pulsanti:
        screen.onkey(lambda key=i: snake.key_pressed(key),i)
    screen.listen()
    
    food= Turtle("circle")
    food.color("red")
    food.up()
    food.speed("fastest")
    food.goto(x=random.randint(-(SCREEN_WIDTH/2 -20),SCREEN_WIDTH/2 -20) //20 *20, y=random.randint(-(SCREEN_HEIGHT/2 -20),SCREEN_HEIGHT/2 -20)//20 *20)

#change food position
def change_food_position():
    #TODO control if the food is not in the snake's body
    #change food position randomly but the number must be a multiple of 20
    food.goto(x=random.randint(-(SCREEN_WIDTH/2 -20),SCREEN_WIDTH/2 -20) //20 *20, y=random.randint(-(SCREEN_HEIGHT/2 -20),SCREEN_HEIGHT/2 -20)//20 *20)
    screen.update()

def check_collision():
    for i in range(len(snake.snake_body)-1,0,-1):
        if snake.snake_head.distance(snake.snake_body[i]) < 10:
            return True
    return False

def game_over():
    global snake
    global food
    global scoreboard
    scoreboard.game_over()
    play_again= screen.textinput("Game Over", "Do you want to play again? (y/n)")
    if play_again == "y":
        #clear scoreboard
        scoreboard.clear()
        #delete the food
        food.hideturtle()
        food=0
        #delete the snake
        snake.snake_head.hideturtle()
        snake.snake_head=0;
        for i in snake.snake_body:
            i.hideturtle()
            i=0
        snake.snake_body.clear()
        snake=0
        #restart the game
        game_setup()
        return False
    else :
        return True

def main():
    isGameOver= False
    game_setup()

    while not isGameOver:
        snake.move()
        time.sleep(0.1)
        #control if the snake is out of the screen
        if snake.snake_head.xcor() > (SCREEN_WIDTH/2 -20) or snake.snake_head.xcor() < -(SCREEN_WIDTH/2 -20) or snake.snake_head.ycor() > (SCREEN_HEIGHT/2 -20) or snake.snake_head.ycor() < -(SCREEN_HEIGHT/2 -20):
            isGameOver= game_over()
        #control snake collision
        if check_collision():
            isGameOver= game_over()
        #control if the snake has eaten the food
        if snake.snake_head.distance(food) < 10:
            change_food_position()
            snake.increase_size()
            scoreboard.increase_score()

    

main()