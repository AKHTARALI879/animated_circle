import turtle
turtle.bgcolor("#060D0D")
turtle.pensize(1)
turtle.speed(0.5)
color = ["#4E9B47", "#FFD700", "#5B5B5B", "#FFF7A7", "#A48111" , "#676767", "#1D3F6E", "#333333", "#CF202A", "#6F295B", "#7AC5CD", "#5D4A44", "#FFD700", "#FF9900", "#60BBD0", "#FFF7A7", "#688335", "#0F4C81", "#8FD0CA", "#F9E6E6", "#CC0000"]

for a in range(100):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.right(5)
turtle.mainloop()
