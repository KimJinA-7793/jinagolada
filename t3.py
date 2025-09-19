import turtle as t  # as => 별칭 

t.bgcolor('black')
t.shape("turtle")
t.color('yellow')

t.penup()
t.goto(100,100)
t.pendown()

angle = 89

for x in range(200):
    t.forward(x)
    t.left(angle)
