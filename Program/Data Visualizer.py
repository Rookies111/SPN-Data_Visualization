# Import library
import turtle
# Class to read data from file
class Data:
    # Method to move turtle pen without line (simular to teleport)
    def warpto(self, pen: turtle.Turtle, coord: tuple[int, int]) -> None:
        pen.up()
        pen.setpos(coord[0], coord[1])
        pen.down()
    # Method to read file and return list of data
    def readFile(self, filename: str) -> list:
        with open(filename, 'r', encoding="UTF-8") as file:
            header = file.readline().rstrip().split(",")
            xAxis, yAxis, color = [header[0]], [header[1]], [header[2]]
            for line in file:
                xValue, yValue, cValue = line.rstrip().split(",")
                xAxis.append(xValue)
                yAxis.append(int(yValue))
                color.append(cValue)
        # Return rough formated data
        return header + xAxis + yAxis + color
# Class to create and display bar chart
class Bar(Data):
    # Constructor
    def __init__(self, data: list):
        # Format data from list to attribute
        header = data[0:3]
        del data[0:3]
        self.xLabel = data.pop(0)
        self.xValue = data[0:data.index(header[1])]
        del data[0:data.index(header[1])]
        self.yLabel = data.pop(0)
        self.yValue = data[0:data.index(header[2])]
        del data[0:data.index(header[2])]
        self.color = data[data.index(header[2])+1:]
        # Create turtle pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
    # Method to display chart
    def display(self, **karg):
        # Sync all default optional value to the recieved optional parameter
        options = {"showgrid": False, "line": 5, "bar": 7.5}
        for key in options.keys():
            if key in karg: options[key] = karg[key]
        # Create 'bar width' variable
        origin =(-300, -260)
        length = len(self.xValue)
        maximum = max(self.yValue)
        # Create x-axis and y-axis
        self.warpto(self.pen, origin)
        self.pen.left(90)
        self.pen.forward(2*abs(origin[1]))
        self.pen.stamp()
        self.warpto(self.pen, (origin[0], abs(origin[1]) + 10))
        self.pen.write(self.yLabel, align="center", font=('Time new roman', 12, 'normal'))
        self.warpto(self.pen, origin)
        self.pen.right(90)
        self.pen.forward(2*abs(origin[0]))
        self.pen.stamp()
        self.warpto(self.pen, (abs(origin[0]) + 10, origin[1] - 10))
        self.pen.write(self.xLabel, align="left", font=('Time new roman', 12, 'normal'))
        # Create x-axis labels
        for i in range(length):
            x = (2*abs(origin[0]) + origin[0]/length)*(i/length) - (abs(origin[0]) + origin[0]/length)
            if options["showgrid"]:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (x, abs(origin[1]) - 10))
                self.pen.goto(x, origin[1] + options["line"])
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (x, origin[1] + options["line"]))
            self.pen.goto(x, origin[1] - options["line"])
            self.warpto(self.pen, (x, origin[1] - 5*options["line"]))
            self.pen.write(self.xValue[i], align="center", font=('Time new roman', 12, 'normal'))
        # Create y-axis labels
        for i in range(10):
            y = (50 * i) + (origin[1] + 50)
            if options["showgrid"]:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (abs(origin[0])-10, y))
                self.pen.goto(origin[0] + options["line"], y)
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (origin[0] + options["line"], y))
            self.pen.goto(origin[0] - options["line"], y)
            self.warpto(self.pen, (origin[0] - options["line"], y - 2*options["line"]))
            self.pen.write(int(maximum*(i+1)/10), align="right", font=('Time new roman', 11, 'normal'))
        # Create each bar in bar graph
        self.pen.left(90)
        self.warpto(self.pen, origin)
        for i in range(length):
            x = (2*abs(origin[0]) + origin[0]/length)*(i/length) - (abs(origin[0]) + origin[0]/length)
            y = 50*self.yValue[i]/int(maximum/10)
            print(i, x, y)
            self.warpto(self.pen, (x-options["bar"]/2, origin[1]))
            self.pen.color('black', self.color[i])
            self.pen.begin_fill()
            self.pen.forward(y)
            self.pen.right(90)
            self.pen.forward(options["bar"])
            self.pen.right(90)
            self.pen.forward(y)
            self.pen.end_fill()
            self.pen.right(180)
        # Hide turtle pen
        self.pen.hideturtle()
# Class to create and display pie chart
class Pie(Data):
    # Constructor
    def __init__(self, data: list):
        # Format data from list to attribute
        header = data[0:3]
        del data[0:3]
        self.xLabel = data.pop(0)
        self.xValue = data[0:data.index(header[1])]
        del data[0:data.index(header[1])]
        self.yLabel = data.pop(0)
        self.yValue = data[0:data.index(header[2])]
        del data[0:data.index(header[2])]
        self.color = data[data.index(header[2])+1:]
        # Create turtle pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
    # Method to display chart
    def display(self, **karg):
        # Sync all default optional value to the recieved optional parameter
        options = {"size": 120}
        for key in options.keys():
            if key in karg: options[key] = karg[key]           
        # Convert all y values to degrees
        degrees = self.yValue.copy()
        for i in range(len(self.yValue)):
            degrees[i] = 360*degrees[i]/sum(self.yValue)
        # Create chart title
        self.warpto(self.pen, (0, -options["size"]/2 -50))
        self.pen.write(self.yLabel, align="center", font=('Time new roman', 30, 'normal'))
        # Create chart legend
        for i in range(len(self.xValue)):
            value = round(100*self.yValue[i]/sum(self.yValue), 2)
            tab_length = 2-len(self.xValue[i])//9 % 7
            self.warpto(self.pen, (-130, -options["size"]/2 - 65-i*20))
            self.pen.color("black", self.color[i])
            self.pen.begin_fill()
            self.pen.setheading(0)
            for j in range(3):
                self.pen.forward(10)
                self.pen.right(90)
            self.pen.forward(10)
            self.pen.end_fill()
            self.warpto(self.pen, (-100, -options["size"]/2 - 80-i*20))
            self.pen.write(self.xValue[i]+'\t'*tab_length+"- "+str(value)+"%", font=('Time new roman', 12, 'normal'))
            self.warpto(self.pen, (-100, -options["size"]/2 - 80-(i+1)*20))
        # Create pie chart
        self.pen.penup()
        self.pen.home()
        for i in range(len(self.color)):
            self.pen.color(self.color[i])
            self.pen.begin_fill()
            self.pen.circle(options["size"], degrees[i])
            self.pen.left(90)
            self.pen.forward(options["size"])
            self.pen.left(180-degrees[i])
            self.pen.forward(options["size"])
            self.pen.end_fill()
            self.pen.left(90)
            self.pen.circle(options["size"], degrees[i])
        # Hide turtle pen
        self.pen.hideturtle()
# Class to create and display line chart
class Line(Data):
    # Constructor
    def __init__(self, data: list):
        # Format data from list to attribute
        header = data[0:3]
        del data[0:3]
        self.xLabel = data.pop(0)
        self.xValue = data[0:data.index(header[1])]
        del data[0:data.index(header[1])]
        self.yLabel = data.pop(0)
        self.yValue = data[0:data.index(header[2])]
        del data[0:data.index(header[2])]
        self.color = data[data.index(header[2])+1:]
        # Create turtle pen
        self.pen = turtle.Turtle()
        self.pen.speed(0)
    # Method to display chart
    def display(self, **karg):
        # Sync all default optional value to the recieved optional parameter
        options = {"showgrid": False, "line": 5, "size": 5}
        for key in options.keys():
            if key in karg: options[key] = karg[key]
        # Create 'bar width' variable
        origin =(-300, -260)
        length = len(self.xValue)
        maximum = max(self.yValue)
        # Create x-axis and y-axis
        self.warpto(self.pen, origin)
        self.pen.left(90)
        self.pen.forward(2*abs(origin[1]))
        self.pen.stamp()
        self.warpto(self.pen, (origin[0], abs(origin[1]) + 10))
        self.pen.write(self.yLabel, align="center", font=('Time new roman', 12, 'normal'))
        self.warpto(self.pen, origin)
        self.pen.right(90)
        self.pen.forward(2*abs(origin[0]))
        self.pen.stamp()
        self.warpto(self.pen, (abs(origin[0]) + 10, origin[1] - 10))
        self.pen.write(self.xLabel, align="left", font=('Time new roman', 12, 'normal'))
        # Create x-axis self.xValue
        for i in range(length):
            x = (2*abs(origin[0]) + origin[0]/length)*(i/length) - (abs(origin[0]) + origin[0]/length)
            if options["showgrid"]:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (x, abs(origin[1]) - 10))
                self.pen.goto(x, origin[1] + options["line"])
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (x, origin[1] + options["line"]))
            self.pen.goto(x, origin[1] - options["line"])
            self.warpto(self.pen, (x, origin[1] - 5*options["line"]))
            self.pen.write(self.xValue[i], align="center", font=('Time new roman', 9, 'normal'))
        # Create y-axis labels
        for i in range(10):
            y = (50 * i) + (origin[1] + 50)
            if options["showgrid"]:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (abs(origin[0])-10, y))
                self.pen.goto(origin[0] + options["line"], y)
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (origin[0] + options["line"], y))
            self.pen.goto(origin[0] - options["line"], y)
            self.warpto(self.pen, (origin[0] - options["line"], y - 2*options["line"]))
            self.pen.write(int(maximum*(i+1)/10), align="right", font=('Time new roman', 11, 'normal'))
        # Create line graph
        self.warpto(self.pen, origin)
        for i in range(length):
            x = (2*abs(origin[0]) + origin[0]/length)*(i/length) - (abs(origin[0]) + origin[0]/length)
            y = 50*self.yValue[i]/int(maximum/10) + origin[1]
            print(i, self.yValue[i], x, y)
            self.pen.goto(x, y)
            self.pen.dot(options["size"], self.color[i])
        # Hide turtle pen
        self.pen.hideturtle()     
# Display chart
chart = Line(Data().readFile("The-Attendances-over-this-week.csv"))
chart.display(showgrid=True)
# Stop execution
turtle.done()