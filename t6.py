import turtle

window = turtle.Screen()

t = turtle.Turtle()
t.penup()

def turn_right():
    t.setheading(0)
    t.forward(10)

def turn_up():
    t.setheading(90)
    t.forward(10)

def turn_left():
    t.setheading(180)
    t.forward(10)

def turn_down():
    t.setheading(270)
    t.forward(10)

def blank():
    t.clear()
    
window.onkeypress(turn_right, "Right")
window.onkeypress(turn_up, "Up")
window.onkeypress(turn_left, "Left")
window.onkeypress(turn_down, "Down")
window.onkeypress(blank, "Escape")

window.listen()  #키 입력 대기
window.mainloop() #창 안 닫히게 ~
