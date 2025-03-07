import turtle             # Allows us to use turtles
wn = turtle.Screen()      # Creates a playground for turtles
ivan = turtle.Turtle()   # Create a turtle, assign to betty

n = int(input("Enter number of sides: "))
for i in range(n):
    # draw a side of the polygon
    ivan.forward(400/n)
    ivan.left(360/n)

wn.mainloop()
