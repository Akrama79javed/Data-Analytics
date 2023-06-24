from turtle import *
speed('fastest')
size = 10
angle = 61
colors = ['red','yellow','black','blue','green','pink']
while True :
    pencolor(colors[size%6])
    fd(size)
    lt(angle)
    size += 1