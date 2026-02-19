import turtle
import random

score = 0
target = None
score_writer = None
time_left = 30
timer_writer = None
game_over = False

def run_target_game(exit_callback=None):
    global score, target, score_writer, timer_writer, time_left, game_over
    screen = turtle.Screen()
    screen.title("Click-to-Target Game")
    screen.bgcolor("lightblue")
    screen.clear()

    # Reset score
    score = 0

    # Setup Target Turtle
    target = turtle.Turtle()
    target.shape("turtle")
    target.color("green")
    target.shapesize(2, 2)
    target.penup()
    
    # Setup Score Writer
    score_writer = turtle.Turtle()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.goto(0, 260)
    score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))

    # Setup Timer Writer
    time_left = 30
    game_over = False
    timer_writer = turtle.Turtle()
    timer_writer.hideturtle()
    timer_writer.penup()
    timer_writer.goto(200, 260)
    timer_writer.write(f"Time: {time_left}", align="center", font=("Arial", 20, "normal"))

    # Instructions
    instruction_writer = turtle.Turtle()
    instruction_writer.hideturtle()
    instruction_writer.penup()
    instruction_writer.goto(0, -280)
    msg = "Click the turtle! "
    if exit_callback:
        msg += "Press ESC to return to Menu."
    else:
        msg += "Close window to Exit."
    instruction_writer.write(msg, align="center", font=("Arial", 12, "bold"))

    def restart_game():
        global score, time_left, game_over
        score = 0
        time_left = 30
        game_over = False
        
        # Reset UI
        score_writer.clear()
        score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
        timer_writer.clear()
        timer_writer.write(f"Time: {time_left}", align="center", font=("Arial", 20, "normal"))
        instruction_writer.clear()
        
        msg = "Click the turtle! "
        if exit_callback:
            msg += "Press ESC to Menu. 'R' to Restart."
        else:
            msg += "Close to Exit. 'R' to Restart."
        instruction_writer.write(msg, align="center", font=("Arial", 12, "bold"))
        
        # Reset Target
        target.showturtle()
        target.shapesize(2, 2)
        target.color("green")
        target.goto(0, 0)
        
        # Restart countdown (check if already running? ontimer cancels previous? No, we need to handle it)
        # Actually, if game_over was True, countdown stopped. If we restart, we need to call it again.
        countdown()

    def countdown():
        global time_left, game_over
        if time_left > 0 and not game_over:
            time_left -= 1
            timer_writer.clear()
            timer_writer.write(f"Time: {time_left}", align="center", font=("Arial", 20, "normal"))
            screen.ontimer(countdown, 1000)
        elif not game_over:
            game_over = True
            target.hideturtle()
            instruction_writer.clear()
            instruction_writer.write("GAME OVER!", align="center", font=("Arial", 30, "bold"))
            timer_writer.clear()
            
    def move_target(x, y):
        global score, game_over
        if game_over:
            return

        # Check distance
        if target.distance(x, y) < 40: # Clicked near the turtle
            score += 1
            score_writer.clear()
            score_writer.write(f"Score: {score}", align="center", font=("Arial", 24, "bold"))
            
            # Visual Feedback: Flash color
            target.color("red")
            screen.ontimer(lambda: target.color("green"), 100)
            
            # Difficulty Scaling: Shrink
            current_size = target.shapesize()[0]
            if current_size > 0.5:
                new_size = current_size * 0.85
                target.shapesize(new_size, new_size)

            # Teleport
            new_x = random.randint(-280, 280)
            new_y = random.randint(-280, 280)
            target.goto(new_x, new_y)
        else:
            # Optional: Penalty or just nothing
            pass

    screen.onclick(move_target)
    countdown()

    if exit_callback:
        screen.onkey(exit_callback, "Escape")
    
    screen.onkey(restart_game, "r")
    screen.onkey(restart_game, "R")
    screen.listen()

if __name__ == "__main__":
    run_target_game()
    turtle.Screen().mainloop()
