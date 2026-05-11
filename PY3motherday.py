import turtle
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black") 
screen.setup(width=800, height=800)
screen.title("Centered Mother's Day Projector")
screen.tracer(0) 

t = turtle.Turtle()
t.hideturtle()

heart_t = turtle.Turtle()
heart_t.hideturtle()
star_t = turtle.Turtle()
star_t.hideturtle()

def draw_star(x, y, size):
    star_t.penup()
    star_t.goto(x, y)
    star_t.color("white")
    star_t.begin_fill()
    for _ in range(5):
        star_t.forward(size)
        star_t.right(144)
    star_t.end_fill()

def draw_heart(tt, x, y, size, color):
    tt.penup()
    tt.goto(x, y)
    tt.color(color)
    tt.fillcolor(color)
    tt.begin_fill()
    tt.setheading(140)
    tt.pendown()
    tt.forward(size)
    for _ in range(200):
        tt.right(1)
        tt.forward(size * 0.009)
    tt.left(120)
    for _ in range(200):
        tt.right(1)
        tt.forward(size * 0.009)
    tt.forward(size)
    tt.end_fill()
    tt.setheading(0)

def draw_lush_flower(x, y, color):
    # Centering logic: move to the center point first
    t.penup()
    t.goto(x, y)
    t.setheading(0)
    t.color(color)
    # Draw petals symmetrically around the (x,y) point
    for _ in range(10):
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.begin_fill()
        t.circle(18, 180)
        t.left(144)
        t.end_fill()
    # Yellow center exactly on (x,y)
    t.penup()
    t.goto(x, y - 8)
    t.color("yellow")
    t.begin_fill()
    t.circle(8)
    t.end_fill()

# --- DRAWING SECTION ---

# 1. Background Stars
stars = [(random.randint(-380, 380), random.randint(-350, 200)) for _ in range(60)]

# 2. HAPPY MOTHER'S DAY (Lowered significantly for visibility)
t.penup()
t.goto(0, 200)
t.color("white")
t.write("HAPPY MOTHER'S DAY!", align="center", font=("Arial", 38, "bold"))

# 3. Bouquet Wrap
t.penup()
t.goto(0, -320)
t.color("powderblue")
t.begin_fill()
t.goto(-40, -180)
t.goto(40, -180)
t.goto(0, -320)
t.end_fill()

# 4. Flowers and Stems (Lowered the whole bouquet)
flower_positions = [
    (-80, -50, "orchid"),
    (-40, 0, "indianred"),
    (0, 20, "white"),
    (40, 0, "orange"),
    (80, -50, "hotpink"),
    (-30, -80, "royalblue"),
    (30, -80, "violet")
]

t.pensize(3)
t.color("forestgreen")
base_y = -250

# Draw Stems
for fx, fy, col in flower_positions:
    t.penup()
    t.goto(0, base_y)
    t.pendown()
    t.goto(fx, fy)

# Draw Flowers (Now using centered logic)
for fx, fy, col in flower_positions:
    draw_lush_flower(fx, fy, col)

# 5. Bottom Text
t.penup()
t.goto(0, -370)
t.color("gold")
t.write("For You, Mom", align="center", font=("Arial", 18, "italic"))

screen.update()

# --- ANIMATION ---
# Top hearts moved down (y=160), bottom hearts adjusted
heart_pos = [(-320, 160, "pink"), (320, 160, "red"), (-320, -250, "purple"), (320, -250, "deeppink")]
size_mod = 0
growing = True

while True:
    heart_t.clear()
    star_t.clear()
    
    for sx, sy in random.sample(stars, 12):
        draw_star(sx, sy, random.randint(2, 4))
    
    if growing:
        size_mod += 0.5
        if size_mod > 10: growing = False
    else:
        size_mod -= 0.5
        if size_mod < 0: growing = True
        
    for x, y, color in heart_pos:
        draw_heart(heart_t, x, y, 45 + size_mod, color)
    
    screen.update()
    time.sleep(0.04)
