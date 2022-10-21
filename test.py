import sys, turtle

def move_list(l):
    for i in l:
        match i[0]:
            case "F":
                t.forward(int(i[1:]))
            case "B":
                t.backward(int(i[1:]))
            case "L":
                t.left(int(i[1:]))
            case "R":
                t.right(int(i[1:]))

def draw_start(pos, c, pc, pensize=0):
    t.setposition(*pos)
    if pensize != 0:
        t.pensize(pensize)
    t.pendown()
    t.begin_fill()
    t.color(c)
    t.pencolor(pc)

def draw_circle(pos, size, c, pc, pensize=0):
    draw_start(pos, c, pc, pensize)
    t.circle(size)
    t.end_fill()
    t.penup()

def draw_A(pos, c, pc, pensize=0):
    draw_start(pos, c, pc, pensize)
    move_list([
        "F23",      "B123",     "L60",      "B220", 
        "R60",      "B100",     "R117",     "B710", 
        "R63",      "B110",     "R90",      "B510", 
        "R90",      "B100",     "R90",      "B70"
    ])
    t.end_fill()
    t.penup()

def draw_TnA(pos, c, pc, pensize=0):
    draw_start(pos, c, pc, pensize)
    move_list(["R90", "F100", "R115", "F250", "R157", "F227"])
    t.end_fill()
    move_list(["B80", "L42",  "F147",  "R83", "F140"])
    t.penup()

if __name__ == '__main__':
    turtle.Screen().bgcolor("black")
    t = turtle.Turtle()
    t.speed(10 if len(sys.argv) < 2 else int(sys.argv[1]))
    t.penup()

    draw_circle((0, -280), 300, "red", "white", 10)
    draw_circle((0, -230), 250, "black", "black", 2)
    draw_circle((0, -200), 200, "black", "white", 2)
    draw_A((30, -110), "red", "white", 10)
    draw_TnA((53, -40), "black", "white", 10)

    t.hideturtle()
    turtle.done()