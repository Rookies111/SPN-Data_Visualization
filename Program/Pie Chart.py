#Libraries used:
import turtle
import time
import requests
import json

class InFormaTion:
    def __init__(self):
        url = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-all"
        response = requests.get(url).text
        data = json.loads(response)
        self.new_recovered = data[0]['new_recovered']
        self.new_case = data[0]['new_case']
        self.new_death = data[0]['new_death']

class ShowCase(InFormaTion):
    def __init__(self):
        super().__init__()

    def display(self):
        #Setting of radius:
        size = 120
        #Setting of labels:
        labels = ["NewCase", "NewRecovered", "NewDeath"]

        #Setting of colors:
        colors =["blue", "green", "red"]
        
        #Generation of values for demonstration:
        some_values = []
        temp = []
        a= self.new_recovered
        b= self.new_case
        c= self.new_death
                
        temp=[a,b,c]
        some_values.append(temp)
                        
        #Conversion of values to shares :
        shares = [x[:] for x in some_values]
        for i in range(0, len(shares)):
            total = sum(shares[i])
            for j in range(0, len(shares[i])):
                shares[i][j] = shares[i][j]/total
        print(shares)
                        
        #Conversion of shares to degrees
        degrees = [x[:] for x in shares ]
        for i in range(0, len(degrees)):
            for j in range(0, len(degrees[i])):
                degrees[i][j] = degrees [i][j]*360
        print(degrees)

        #Creation of title of chart:
        t_name = turtle.Pen()
        t_name.speed(1000)
        t_name.penup()
        t_name.goto(0,-size / 2)
        t_name.pendown()
        t_name.write("My bar chart race in Turtie ",align="center" , font=150)
        t_name.hideturtle()
        #Initialization of pen for legend:
        t_legend = turtle.Pen()
        #Initialization of pen for counter of periods:
        t_period = turtle.Pen()
        #Initialization of pens for drawing of pie chart:
        t_1=turtle.Pen()
        t_2=turtle.Pen()
        for i in range(0, len(degrees)):
        #Updating of counter of periods:
            t_period.speed(1000)
            t_period.penup()
            t_period.goto(2* size,0)
            t_period.down()
            t_period.write("Period"+str(i+1))
            t_period.hideturtle()

        #Updating of legend:
            t_legend.speed(1000)
            t_legend.penup()
            t_legend.goto(-2.5 * size,50)
            for j in range(0, len(labels)):
                t_legend.color(colors[j])
                t_legend.write(labels [j]+ "-" + str(round(100*shares[i][j],2)))
                t_legend.goto(-2.5*size, 50-(j+1)*20)
            t_legend.hideturtle()

        #Updating of pie chart:
            t_1.speed(1000)
            t_1.hideturtle()
            t_2.speed(1000)
            t_2.hideturtle()
            if i%2==0:
                for j in range(0, len(colors)):
                    t_1.color(colors[j])
                    t_1.begin_fill()
                    t_1.circle(size, degrees[i][j])
                    t_1.left(90)
                    t_1.forward(size)
                    t_1.left(180-degrees[i][j])
                    t_1.forward(size)
                    t_1.end_fill()
                    t_1.left(90)
                    t_1.circle(size, degrees[i][j])
                        

            #Reseting of pen for drawing of pie chart:
            t_2.reset()
        else:
            for j in range(0, len(colors)):
                t_2.color(colors[j])
                t_2.begin_fill()
                t_2.circle(size,degrees[i][j])
                t_2.left(90)
                t_2.forward(size)
                t_2.left(180-degrees[i][j])
                t_2.forward(size)
                t_2.end_fill()
                t_2.left(90)
                t_2.circle(size, degrees[i][j])
        #Reseting of pen for drawing of pie chart:
                t_1.reset()
        #Pause:
            time.sleep(1)
        #Reseting of pens for legend and counter of periods:
        t_period.reset()
        t_legend.reset()

ShowCase().display()
