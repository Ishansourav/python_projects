import turtle as t

def draw_circle(color, x, y, radius):
    t.penup()
    t.fillcolor(color)
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_panda():
    t.speed(0)
    t.bgcolor("#FDD7E4")
    
    # Draw head
    draw_circle("black", 0, 0, 100)

    # Draw eyes
    draw_circle("white", -35, 120, 20)
    draw_circle("white", 35, 120, 20)
    draw_circle("black", -35, 120, 10)
    draw_circle("black", 35, 120, 10)

    # Draw nose
    draw_circle("white", 0, 60, 12)

    # Draw ears
    draw_circle("black", -70, 150, 30)
    draw_circle("black", 70, 150, 30)

    # Draw body
    draw_circle("black", 0, -100, 80)

    # Draw arms
    draw_circle("black", -70, -40, 25)
    draw_circle("black", 70, -40, 25)

    # Draw legs
    draw_circle("black", -40, -180, 25)
    draw_circle("black", 40, -180, 25)

    t.done()

if __name__ == "__main__":
    draw_panda()

