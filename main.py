import turtle
from sketchpad import start_sketchpad
from race import run_race
from target_game import run_target_game
import sys

# Setup screen once
screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Project: Sketchpad, Race, & Target Game")

def show_menu():
    try:
        screen.clearscreen() # Reset everything including background
        screen.bgcolor("white")
        screen.tracer(1) # Ensure animations are on
        
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed(0)
        pen.penup()
        
        pen.goto(0, 100)
        pen.write("Turtle Project Menu", align="center", font=("Arial", 24, "bold"))
        
        pen.goto(0, 30)
        pen.write("1. Interactive Sketchpad", align="center", font=("Arial", 16, "normal"))
        
        pen.goto(0, 0)
        pen.write("2. Turtle Race", align="center", font=("Arial", 16, "normal"))
        
        pen.goto(0, -30)
        pen.write("3. Target Game", align="center", font=("Arial", 16, "normal"))
        
        pen.goto(0, -80)
        pen.write("Press 1, 2, or 3 to select. Press Q to Quit.", align="center", font=("Arial", 12, "italic"))

        def run_feature(feature_func):
            screen.clearscreen()
            feature_func(show_menu)

        # Key bindings for menu
        screen.onkey(lambda: run_feature(start_sketchpad), "1")
        screen.onkey(lambda: run_feature(run_race), "2")
        screen.onkey(lambda: run_feature(run_target_game), "3")
        screen.onkey(turtle.bye, "q")
        screen.onkey(turtle.bye, "Q")
        
        screen.listen()
    except Exception as e:
        print(f"Error in menu: {e}")
        # If screen is destroyed, just exit
        sys.exit()

if __name__ == "__main__":
    show_menu()
    turtle.mainloop()
