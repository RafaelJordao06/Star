import turtle
sc=turtle.Screen()
sc.setup(600,600)
spiral = turtle.Turtle()
spiral.speed(7)
sc.bgcolor("black")
cor=["red","red","red","red"]
c=0
for i in range(1000):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(cor[c])
    if c==3:
        c=0
    else:
        c+=1