import random as r
import math as m

def writeCode(code,filename="latest"):
    file = open(filename+".txt", "w")
    file.write(code)
    file.close()

def compileCode(lines, scenery="", bonus="", bike="BMX"):
    return lines + "#" + scenery + "#" + bonus + "#" + bike

def str_base(num, base = 32, numerals = '0123456789abcdefghijklmnopqrstuvwxyz'):
    if type(num) == float:
        num = int(num)
    if num == 0:
        return '0'
    sign = ''
    if num < 0:
        sign = '-'
        num = -num
    result = ''
    while num:
        result = numerals[num % (base)] + result
        num //= base
    return sign + result
    
def connect(coordinates,end=","):
    code = ""
    for (x,y) in coordinates:
        code += str_base(x) + " " + str_base(y) + " "
    return code+end

def gravity(x,y,alpha,end=","): #alpha -> degrees
    return "G " + str_base(x) + " " + str_base(y) + " " + str_base(alpha) + end
    
def boost(x,y,alpha,end=","):
    return "B " + str_base(x) + " " + str_base(y) + " " + str_base(alpha) + end
    
def goal(x,y,end=","):
    return "T " + str_base(x) + " " + str_base(y) + end
    
def checkpoint(x,y,end=","):
    return "C " + str_base(x) + " " + str_base(y) + end
    
def bomb(x,y,end=","):
    return "O " + str_base(x) + " " + str_base(y) + end

def line(x1,y1,x2,y2,end=","):
    return connect([(x1,y1),(x2,y2)],end)

def rect(x,y,width,height,end=","):
    return connect([(x,y),(x,y+height),(x+width,y+height),(x+width,y),(x,y)],end)
    
def triangle(x1,y1,x2,y2,x3,y3,end=","):
    return connect([(x1,y1),(x2,y2),(x3,y3),(x1,y1)],end)
    
def arc(x,y,rx,ry,start=0,stop=2*m.pi,end=",",prcs=2*m.pi/50):
    coordinates = []
    alpha = start
    while alpha < stop:
        coordinates+=[(x+rx*m.cos(alpha),y+ry*m.sin(alpha))]
        alpha += prcs
    return connect(coordinates,end) if abs(start-stop) < 2*m.pi else connect(coordinates+[coordinates[0]],end)
    
def ellipse(x,y,rx,ry,end=",",prcs=-1):
    if prcs < 0:
        prcs = 4*m.pi/(m.log(rx*rx+ry*ry)*m.log(rx*rx+ry*ry))
    return arc(x,y,rx,ry,0,2*m.pi,end,prcs)
    
def curve_of_function(f, values):
    return line([(value,f(value)) for value in values])
