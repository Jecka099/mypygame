import turtle
import random

# Set up the screen
screen = turtle.Screen()
screen.title("Turtle Catch Game with Turning, Obstacles, Scoring, and Game Over")
screen.bgcolor("lightblue")
screen.setup(width=800, height=600)

# Create the player turtle
player = turtle.Turtle()
player.shape("turtle")
player.color("green")
player.penup()
player.speed(0)

# Create the target
target = turtle.Turtle()
target.shape("circle")
target.color("red")
target.penup()
target.speed(0)
target.setposition(random.randint(-380, 380), random.randint(-290, 290))

# Create obstacles
obstacles = []
for _ in range(5):  # Create 5 obstacles
    obstacle = turtle.Turtle()
    obstacle.shape("square")
    obstacle.color("blue")
    obstacle.penup()
    obstacle.speed(0)
    obstacle.setposition(random.randint(-380, 380), random.randint(-290, 290))
    obstacles.append(obstacle)

# Create a score display
score = 0
score_display = turtle.Turtle()
score_display.hideturtle()
score_display.penup()
score_display.color("black")
score_display.goto(0, 260)
score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Create a game over display
game_over_display = turtle.Turtle()
game_over_display.hideturtle()
game_over_display.penup()
game_over_display.color("red")
game_over_display.goto(0, 0)

# Functions to control the player turtle
def move_forward():
    player.forward(20)

def move_backward():
    player.backward(20)

def turn_left():
    player.left(30)  # Turn left by 30 degrees

def turn_right():
    player.right(30)  # Turn right by 30 degrees

# Check for collision with the target
def check_collision_with_target():
    global score
    if player.distance(target) < 20:
        target.setposition(random.randint(-380, 380), random.randint(-290, 290))
        score += 1
        score_display.clear()
        score_display.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# Check for collision with obstacles
def check_collision_with_obstacles():
    for obstacle in obstacles:
        if player.distance(obstacle) < 20:
            return True
    return False

# Display the "Game Over" message
def display_game_over():
    game_over_display.write("Game Over!", align="center", font=("Arial", 36, "bold"))

# Set up key bindings
screen.listen()
screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

# Main game loop
game_over = False
while not game_over:
    screen.update()
    check_collision_with_target()
    if check_collision_with_obstacles():
        display_game_over()
        game_over = True

# Close the window after a brief pause to let the message be visible
screen.ontimer(screen.bye, 2000)  # Close the screen after 2 seconds
