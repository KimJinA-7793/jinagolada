import turtle as t  # as => 별칭 
import random

t.bgcolor('pink')
t.shape("turtle")
t.speed(0)
t.color('lime')

for x in range(10):
    a = random.randint(1,360)
    t.setheading(a)
    t.forward(100)
