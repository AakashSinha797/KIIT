import turtle

pen = turtle.Pen()

pen.up();pen.backward(250);pen.down()

pen.color('red', 'yellow')
pen.speed(0)

pen.begin_fill()

for _ in range(300):
	pen.forward(500)
	pen.left(171)

pen.end_fill()

turtle.exitonclick()