# Import library
import requests
import json
import turtle
# Class for other class to inherit method and attributes from
class Misc:
    # Constructor
    def __init__(self):
        # Create attribute
        url = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all"
        response = requests.get(url).text
        self.response_info = json.loads(response)
        self.origin = (-300, -260)
        self.maximum = 0
        for key in ["new_case"]:
            if max(self.allTimeData(key)) > self.maximum:
                self.maximum = max(self.allTimeData(key))
    # Method to teleport 'pen' to designate 'coord'(coordinate)
    def warpto(self, pen: turtle.Turtle, coord: tuple[int, int]) -> None:
        pen.up()
        pen.setpos(coord[0], coord[1])
        pen.down()
    # Method to get data of all the week from 'key'
    def allTimeData(self, key):
        allTimeData_list = []
        for i in range(len(self.response_info)):
            allTimeData_list.append(self.response_info[i][key])
        return allTimeData_list
    # Method to get that week data from 'week' and 'key'
    def weeklyData(self, week, key):
        return self.response_info[week][key]
# Class from create bar graph
class Graph(Misc):
    # Constructor
    def __init__(self, key: str):
        # Inherit data from parent class(Misc)
        super().__init__()
        # Create attribute
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.data = self.allTimeData(key)
        self.length = len(self.data)
    # Method to display graph
    def display(self, color: str) -> None:
        # Create 'bar width' variable
        bar_length = 10
        # Create each bar in bar graph
        self.pen.left(90)
        for i in range(self.length):
            x = (2*abs(self.origin[0]) + self.origin[0]/self.length)*(i/self.length) - (abs(self.origin[0]) + self.origin[0]/self.length)
            y = 50*self.data[i]/int(self.maximum/10)
            print(i, x, y)
            self.warpto(self.pen, (x-bar_length/2, self.origin[1]))
            self.pen.color('black', color)
            self.pen.begin_fill()
            self.pen.forward(y)
            self.pen.right(90)
            self.pen.forward(bar_length)
            self.pen.right(90)
            self.pen.forward(y)
            self.pen.end_fill()
            self.pen.right(180)
        # Hide turtle pen
        self.pen.hideturtle()
# Class from create graph scale
class Scale(Misc):
    # Constructor
    def __init__(self, x_label="", y_label=""):
        # Inherit data from parent class(Misc)
        super().__init__()
        # Create attribute
        self.pen = turtle.Turtle()
        self.pen.speed(0)
        self.label = {'x': x_label, 'y': y_label}
        self.length = len(self.response_info)
        self.week = []
        for i in range(1, self.length+1):
            self.week.append(i)
    # Method to display graph scale
    def display(self, show_grid=False) -> None:
        # Create 'line length' variable
        line_length = 5
        # Create x-axis and y-axis
        self.warpto(self.pen, self.origin)
        self.pen.left(90)
        self.pen.forward(2*abs(self.origin[1]))
        self.pen.stamp()
        self.warpto(self.pen, (self.origin[0], abs(self.origin[1]) + 10))
        self.pen.write(self.label['y'], align="center", font=('Time new roman', 12, 'normal'))
        self.warpto(self.pen, self.origin)
        self.pen.right(90)
        self.pen.forward(2*abs(self.origin[0]))
        self.pen.stamp()
        self.warpto(self.pen, (abs(self.origin[0]) + 10, self.origin[1] - 10))
        self.pen.write(self.label['x'], align="left", font=('Time new roman', 12, 'normal'))
        # Create x-axis labels
        for i in range(self.length):
            x = (2*abs(self.origin[0]) + self.origin[0]/self.length)*(i/self.length) - (abs(self.origin[0]) + self.origin[0]/self.length)
            if show_grid:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (x, abs(self.origin[1]) - 10))
                self.pen.goto(x, self.origin[1] + line_length)
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (x, self.origin[1] + line_length))
            self.pen.goto(x, self.origin[1] - line_length)
            self.warpto(self.pen, (x, self.origin[1] - 5*line_length))
            self.pen.write(self.week[i], align="center", font=('Time new roman', 9, 'normal'))
        # Create y-axis labels
        for i in range(10):
            y = (50 * i) + (self.origin[1] + 50)
            if show_grid:
                self.pen.pencolor("grey")
                self.warpto(self.pen, (abs(self.origin[0])-10, y))
                self.pen.goto(self.origin[0] + line_length, y)
                self.pen.pencolor("black")
            else:
                self.warpto(self.pen, (self.origin[0] + line_length, y))
            self.pen.goto(self.origin[0] - line_length, y)
            self.warpto(self.pen, (self.origin[0] - line_length, y - 2*line_length))
            self.pen.write(int(self.maximum*(i+1)/10), align="right", font=('Time new roman', 11, 'normal'))
        # Hide turtle pen
        self.pen.hideturtle()
# Construct 'Scale' and new case 'Graph'
scale = Scale("Week", "New Case")
newCase = Graph("new_case")
newRecovered = Graph("new_recovered")
# Display scale and new case graph
scale.display(True)
newCase.display("#CC33DD")
newRecovered.display("#00CC00")
# Stop execution
turtle.done()