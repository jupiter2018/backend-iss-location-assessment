#!/usr/bin/env python

__author__ = 'jupiter2018'

import requests
import turtle
import time


def astronaut_list():
    """ get list of astronauts currently in space """
    list_of_astronauts = {}
    mydata = requests.get('http://api.open-notify.org/astros.json')
    if(mydata.status_code == 200):
        if mydata.json():
            astronauts = []
            list_of_astronauts['Number of astronauts'] = mydata.json()[
                'number']
            for i in range(len(mydata.json()['people'])):
                astronauts.append(
                    {'Craft': mydata.json()['people'][i]['craft'].encode('ascii'),
                     'Name': mydata.json()['people'][i]['name'].encode('ascii')})
            list_of_astronauts['Astronauts'] = astronauts
            return list_of_astronauts
        else:
            return "Data not available"


def get_location():
    cur_coord = {}
    mydata = requests.get('http://api.open-notify.org/iss-now.json')
    if(mydata.status_code == 200):
        if mydata.json():
            cur_coord['timestamp'] = mydata.json()[
                'timestamp']
            cur_coord['latitude'] = mydata.json()[
                'iss_position']['latitude'].encode('ascii')
            cur_coord['longitude'] = mydata.json()[
                'iss_position']['longitude'].encode('ascii')
            return cur_coord
        else:
            return "Data not available"


def get_next_pass():
    mydata = requests.get('http://api.open-notify.org/iss-pass.json?lat=39.76&lon=-86.15')
    if(mydata.status_code == 200):
        if mydata.json():
            time_of_pass = mydata.json()['response'][0]['risetime']
            return time.ctime(time_of_pass)
        else:
            return 'Data not available'


def create_turtle():
    wn = turtle.Screen()
    wn.setup(750, 350)
    wn.setworldcoordinates(-180, -90, 180, 90)
    wn.title('ISS location')
    print(wn.screensize())
    wn.bgpic('map.gif')
    tim = turtle.Turtle()
    wn.addshape('iss.gif')
    tim.shape('iss.gif')
    tim.home()
    tim.setheading(45)
    tim.showturtle()
    tim.pendown()
    x_coord = float(get_location()['longitude'])
    y_coord = float(get_location()['latitude'])
    tim.speed(1)
    tim.goto(x_coord, y_coord)
    indy = turtle.Turtle()
    indy.hideturtle()
    indy.penup()
    indy.speed(0)
    indy.setposition(-86.1581, 39.7684)
    indy.dot(10, 'yellow')
    visit = turtle.Turtle()
    visit.hideturtle()
    visit.penup()
    visit.speed(0)
    visit.color('red')
    visit.setposition(-86.1581, 39.7684)
    visit.write(get_next_pass(), font=("Arial", 20, "normal"))
    turtle.mainloop()


def main():
    print(astronaut_list())
    print(get_location())
    create_turtle()


if __name__ == '__main__':
    main()
