import turtle
import math

DRAW_AREA = (0, -50)  # Center of drawing area

def draw_sunflower(draw_turtle, petal_color="orange", center_color="brown", petal_count=60, petal_length=120, petal_width=40):
    t = draw_turtle
    t.clear()
    t.penup()
    t.goto(DRAW_AREA)
    t.setheading(0)
    t.pendown()
    t.speed(0)
    t.hideturtle()
    # Draw petals in a circle
    for i in range(petal_count):
        angle = 360 / petal_count * i
        t.penup()
        t.goto(DRAW_AREA)
        t.setheading(angle)
        t.forward(petal_length)
        t.pendown()
        t.color(petal_color)
        t.begin_fill()
        t.left(45)
        t.circle(petal_width, 90)
        t.left(90)
        t.circle(petal_width, 90)
        t.left(45)
        t.end_fill()
        t.penup()
        t.goto(DRAW_AREA)
        t.setheading(0)
    # Draw center core (inside the petals)
    core_radius = petal_length * 0.55
    t.goto(DRAW_AREA[0], DRAW_AREA[1] - core_radius)
    t.pendown()
    t.color(center_color)
    t.begin_fill()
    t.circle(core_radius)
    t.end_fill()
    t.penup()
    # Draw seeds (dots) inside the core using the golden angle
    t.color("goldenrod")
    for n in range(200):
        angle = n * 137.5  # Golden angle
        radius = math.sqrt(n) * (core_radius * 0.95) / math.sqrt(200)
        x = DRAW_AREA[0] + radius * math.cos(math.radians(angle))
        y = DRAW_AREA[1] + radius * math.sin(math.radians(angle))
        t.goto(x, y)
        t.dot(6)
    t.hideturtle()

def draw_yin_yang(draw_turtle, size=100):
    t = draw_turtle
    t.clear()
    t.penup()
    t.goto(DRAW_AREA[0], DRAW_AREA[1] - size)
    t.pendown()
    t.speed(0)
    t.hideturtle()
    t.color("black", "white")
    t.begin_fill()
    t.circle(size, 180)
    t.circle(size/2, 180)
    t.circle(-size/2, 180)
    t.end_fill()
    t.begin_fill()
    t.color("black", "black")
    t.circle(size, 180)
    t.circle(size/2, 180)
    t.circle(-size/2, 180)
    t.end_fill()
    # Small dots
    t.penup()
    t.goto(DRAW_AREA[0], DRAW_AREA[1] + size/2)
    t.dot(size/5, "black")
    t.goto(DRAW_AREA[0], DRAW_AREA[1] - size/2)
    t.dot(size/5, "white")

def draw_koch_segment(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_snowflake(draw_turtle, size=200, level=3, color="skyblue"):
    t = draw_turtle
    t.clear()
    t.penup()
    t.goto(DRAW_AREA[0] - size/2, DRAW_AREA[1] + size/3)
    t.pendown()
    t.speed(0)
    t.hideturtle()
    t.color(color, "lightblue")
    t.begin_fill()
    for _ in range(3):
        draw_koch_segment(t, size, level)
        t.right(120)
    t.end_fill()

def draw_shape(draw_turtle, shape):
    draw_turtle.clear()
    t = draw_turtle
    t.penup()
    t.goto(DRAW_AREA)
    t.setheading(0)
    t.pendown()
    t.speed(0)
    t.hideturtle()
    # Prompt for color
    color = turtle.textinput("Choose Color", "Enter a color name (e.g. red, blue, green):")
    if not color:
        color = "white"
    if shape == "Square":
        t.color(color)
        for _ in range(4):
            t.forward(100)
            t.right(90)
    elif shape == "Triangle":
        t.color(color)
        for _ in range(3):
            t.forward(100)
            t.right(120)
    elif shape == "Circle":
        t.color(color)
        t.circle(50)
    elif shape == "Sunflower":
        draw_sunflower(draw_turtle, petal_color=color)
        return
    elif shape == "Yin-Yang":
        # Use selected color as the white part, and black as the other
        draw_yin_yang(draw_turtle, size=100)
        # Optionally, you can modify draw_yin_yang to accept color arguments
        return
    elif shape == "Snowflake":
        draw_snowflake(draw_turtle, color=color)
        return
    
    
def gui():
    screen = turtle.Screen()
    screen.title("Turtle Shape GUI")
    screen.bgcolor("black")
    screen.setup(width=1280, height=800)
    # Button positions and labels
    # Window is 1280x720, so center is (0,0), bottom is y=-360
    # Place Exit button centered at the bottom, just above the window edge
    buttons = [
        {"label": "Square", "pos": (-400, 200)},
        {"label": "Triangle", "pos": (-150, 200)},
        {"label": "Circle", "pos": (100, 200)},
        {"label": "Sunflower", "pos": (350, 200)},
        {"label": "Yin-Yang", "pos": (-150, 120)},
        {"label": "Snowflake", "pos": (100, 120)},
        {"label": "Exit", "pos": (-60, -320)},  # Centered at bottom
    ]
    # Draw buttons with a dedicated turtle
    btn_turtles = []
    btn_drawer = turtle.Turtle()
    btn_drawer.hideturtle()
    btn_drawer.penup()
    btn_drawer.speed(0)
    def draw_button(label, pos):
        btn_drawer.goto(pos)
        btn_drawer.pendown()
        btn_drawer.color("white", "#222")
        btn_drawer.begin_fill()
        for _ in range(2):
            btn_drawer.forward(120)
            btn_drawer.right(90)
            btn_drawer.forward(40)
            btn_drawer.right(90)
        btn_drawer.end_fill()
        btn_drawer.penup()
        btn_drawer.goto(pos[0]+60, pos[1]-25)
        btn_drawer.color("white")
        btn_drawer.write(label, align="center", font=("Arial", 14, "bold"))
        btn_drawer.penup()
        btn_turtles.append((label, pos))
    for b in buttons:
        draw_button(b["label"], b["pos"])
    # Drawing turtle (for shapes)
    draw_turtle = turtle.Turtle()
    draw_turtle.hideturtle()
    draw_turtle.speed(0)
    draw_turtle.penup()
    draw_turtle.goto(DRAW_AREA)
    draw_turtle.pendown()
    # Mouse click handler
    def on_click(x, y):
        for label, pos in btn_turtles:
            x0, y0 = pos
            if x0 <= x <= x0+120 and y0-40 <= y <= y0:
                if label == "Exit":
                    turtle.bye()
                else:
                    draw_shape(draw_turtle, label)
                break
    screen.onclick(on_click)
    turtle.done()

if __name__ == "__main__":
    gui()
    
    
    
    
    