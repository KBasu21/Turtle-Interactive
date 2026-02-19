import turtle

def init_sketchpad():
    """Initializes the sketchpad settings."""
    screen = turtle.Screen()
    screen.title("Interactive Sketchpad")
    screen.bgcolor("white")
    
    turtle.hideturtle() # Hide the turtle as requested
    turtle.speed(0)
    turtle.width(2)
    screen.tracer(0) # Disable auto-animation for instant drawing
    return screen

def update_screen():
    turtle.update()

def move_forward():
    turtle.forward(10)
    update_screen()

def turn_left():
    turtle.left(10)
    update_screen()

def turn_right():
    turtle.right(10)
    update_screen()

def move_backward():
    turtle.backward(10)
    update_screen()

def pen_up():
    turtle.penup()

def pen_down():
    turtle.pendown()

def clear_screen():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()
    update_screen()

def set_color_red():
    turtle.color("red")

def set_color_green():
    turtle.color("green")

def set_color_blue():
    turtle.color("blue")

def set_color_black():
    turtle.color("black")

def set_color_orange():
    turtle.color("orange")

def set_color_yellow():
    turtle.color("yellow")

def set_color_purple():
    turtle.color("purple")

def set_color_white():
    turtle.color("white") # Good for erasing if background is white

def increase_size():
    w = turtle.width()
    turtle.width(w + 1)
    update_screen()

def decrease_size():
    w = turtle.width()
    if w > 1:
        turtle.width(w - 1)
    update_screen()

def drag_handler(event):
    x = event.x - turtle.window_width() // 2
    y = (turtle.window_height() // 2) - event.y
    turtle.goto(x, y)
    update_screen()

def click_handler(event):
    x = event.x - turtle.window_width() // 2
    y = (turtle.window_height() // 2) - event.y
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    update_screen()

def start_sketchpad(exit_callback=None):
    """Sets up and runs the interactive sketchpad."""
    screen = init_sketchpad()
    
    # Check if we are running in a main loop or standalone
    # For now, let's assume standard turtle setup but robust enough to be imported
    
    # Key bindings
    screen.listen()
    screen.onkey(move_forward, "Up")
    screen.onkey(move_backward, "Down")
    screen.onkey(turn_left, "Left")
    screen.onkey(turn_right, "Right")
    
    screen.onkey(pen_up, "u")
    screen.onkey(pen_up, "U") # Handle both cases
    screen.onkey(pen_down, "d")
    screen.onkey(pen_down, "D")
    
    screen.onkey(clear_screen, "space")
    
    screen.onkey(set_color_red, "r")
    screen.onkey(set_color_red, "R")
    screen.onkey(set_color_green, "g")
    screen.onkey(set_color_green, "G")
    screen.onkey(set_color_blue, "b")
    screen.onkey(set_color_blue, "B")
    screen.onkey(set_color_black, "k") # 'k' for black as 'b' is blue
    screen.onkey(set_color_black, "K")
    
    screen.onkey(set_color_orange, "o")
    screen.onkey(set_color_orange, "O")
    screen.onkey(set_color_yellow, "y")
    screen.onkey(set_color_yellow, "Y")
    screen.onkey(set_color_purple, "p")
    screen.onkey(set_color_purple, "P")
    screen.onkey(set_color_white, "w")
    screen.onkey(set_color_white, "W")

    # Brush size bindings
    screen.onkey(increase_size, "+")
    screen.onkey(increase_size, "=") # + is usually Shift+=
    screen.onkey(decrease_size, "-")
    screen.onkey(decrease_size, "_")

    # Mouse bindings (Canvas level for free drawing)
    canvas = screen.getcanvas()
    canvas.bind("<B1-Motion>", drag_handler)
    canvas.bind("<Button-1>", click_handler)

    if exit_callback:
        screen.onkey(exit_callback, "Escape")
        exit_msg = " | Press ESC to return to Menu"
    else:
        exit_msg = " | Click to Exit"

    # Instructions
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.penup()
    writer.goto(-280, 260)
    writer.write("Sketchpad: Drag to Draw. +/- for Size. Colors: R, G, B, K, O, Y, P, W." + exit_msg, font=("Arial", 10, "normal"))
    
    update_screen()

if __name__ == "__main__":
    start_sketchpad()
    turtle.Screen().exitonclick()
