import turtle as t
import random

#te = 악당 거북이, ts = 나

te = t.Turtle()
te.shape('turtle')
te.color('red')
te.speed(0)
te.up()
te.goto(0,200)

ts = t.Turtle()
ts.shape('circle')
ts.color('green')
ts.speed(0)
ts.up()
ts.goto(0,-200)

def turn_right():
    t.setheading(0)

def turn_up():
    t.setheading(90)

def turn_left():
    t.setheading(180)

def turn_down():
    t.setheading(270)

def play():
    t.forward(10)
    ang = te.towards(t.pos())   #내 거북이가 방향을 따라가도록 개선해주는..?뭐래 아아 t.포지션으로 향하게 해주는
    te.setheading(ang)
    te.forward(9)

    if t.distance(ts) < 12:    #먼함수임? 먹이를 먹었으면, 그다음 새로운 목표를 설정하는 것. (뭐래노..)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)

    if t.distance(te) >= 12:
        t.ontimer(play, 100)   #on으로 시작하는 함수 = 무조건 이벤트 핸들러

t.setup(500,500)
t.bgcolor('orange')
t.shape('turtle')
t.speed(0)
t.up()  #테두리 안 보이게 하는 것
t.color('white')

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")

t.listen()
play()





        
