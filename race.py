import turtle
import random

def run_race(exit_callback=None):
    screen = turtle.Screen()
    screen.title("Turtle Race")
    screen.clear()
    screen.bgcolor("white")
    
    # Setup race track
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    y_positions = [-100, -60, -20, 20, 60, 100]
    all_turtles = []

    # Draw Finish Line
    ref = turtle.Turtle()
    ref.penup()
    ref.goto(230, -150)
    ref.pendown()
    ref.goto(230, 150)
    ref.hideturtle()

    # Instructions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(0, 260)
    msg = "Turtle Race | Enter bet in popup to start. "
    if exit_callback:
        msg += "Click or ESC to Menu."
    else:
        msg += "Click to Exit."
    writer.write(msg, align="center", font=("Arial", 12, "bold"))
    
    # Create turtles
    for turtle_index in range(0, 6):
        new_turtle = turtle.Turtle(shape="turtle")
        new_turtle.color(colors[turtle_index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[turtle_index])
        all_turtles.append(new_turtle)

    # User bet
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    
    if user_bet:
        is_race_on = True
    else:
        is_race_on = False

    while is_race_on:
        for turtle_runner in all_turtles:
            if turtle_runner.xcor() > 230:
                is_race_on = False
                winning_color = turtle_runner.pencolor()
                if winning_color == user_bet.lower():
                    result_text = f"You've won! The {winning_color} turtle is the winner!"
                else:
                    result_text = f"You've lost! The {winning_color} turtle is the winner!"
                
                # Show result
                ref.penup()
                ref.goto(0, 0)
                ref.write(result_text, align="center", font=("Arial", 16, "bold"))
                print(result_text)

            rand_distance = random.randint(0, 10)
            turtle_runner.forward(rand_distance)
            
    # Bind restart
    screen.onkey(lambda: run_race(exit_callback), "r")
    screen.onkey(lambda: run_race(exit_callback), "R")
    screen.listen()

    # Update instructions for restart
    writer.clear()
    msg = "Race Finished! "
    if exit_callback:
        msg += "Click/ESC to Menu. 'R' to Restart."
    else:
        msg += "Click to Exit. 'R' to Restart."
    writer.write(msg, align="center", font=("Arial", 12, "bold"))

    if exit_callback:
        screen.onclick(lambda x, y: exit_callback())
        # Also bind Escape
        screen.onkey(exit_callback, "Escape")
        screen.listen()
    else:
        # Standalone
        pass

if __name__ == "__main__":
    run_race()
    turtle.Screen().exitonclick()
