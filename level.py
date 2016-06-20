try:
    from freerider2tools import *
except:
    print("ouverture depuis pyzo mal foutue")

def randomBloc(x,y,width,height,end=","):
    code = rect(x,y,width,height,end)
    pic,h = r.randint(0,15),r.random()
    if(pic < 2):
        code += triangle(x,y+pic*height,x+width/2,y+pic*height*(1+h)-h*height/2,x+width,y+pic*height)
    elif(pic < 4):
        pic -= 2
        code += triangle(x+pic*width,y,x+pic*width*(1+h)-h*width/2,y+height/2,x+pic*width,y+height)
            
    for i in range(width-1, 5, -1):
        if(r.randint(0,20)==0):
            code += rect(x+i,y+i,width-2*i,height-2*i,end)
    return code
    
def randomOrb(x,y,width,height,end=","):
    code = ellipse(x,y,width,height,end)
    for i in range(int(width-1), 5, -1):
        if(r.randint(0,20)==0):
            code += ellipse(x,y,width-i,height-i,end)
    return code

def chunck(n,width,height,columns,rows,initial=False):
    code = ""
    if(initial):
        code += "-18 1i 18 1i,-1d 1n 1d 1n 18 1i,-1d 1s 1d 1s 18 1n,-18 1i -1d 1n,-18 1n -1d 1s,"
    scenery = ""
    special = ""
    for i in range(n):
        bonus = r.randint(0,25)
        if(bonus==0):
            special += boost(width/2 + width*r.randint(-columns,columns), height/2 + height*r.randint(-rows,rows), 90*r.randint(0,3))
        elif(bonus==1):
            special += bomb(width/2 + width*r.randint(-columns,columns), height/2 + height*r.randint(-rows,rows))
        elif(bonus<4):
            special += gravity(width/2 + width*r.randint(-columns,columns), height/2 + height*r.randint(-rows,rows), 90*r.randint(0,3))
        elif(bonus<6):
            special += checkpoint(width/2 + width*r.randint(-columns,columns), height/2 + height*r.randint(-rows,rows))
        bloc = r.randint(0,5)
        if(bloc==0):
            code += randomOrb(width/2+width*r.randint(-columns,columns),height/2+height*r.randint(-rows,rows),width/2,height/2)
        else:
            code += randomBloc(width*r.randint(-columns,columns),height*r.randint(-rows,rows),width,height)
        scenery += randomBloc(width*r.randint(-columns,columns),height*r.randint(-rows,rows),width,height)

    return code, scenery, special

a,b,c = chunck(10*10,85,85,10,10,True)
writeCode(compileCode(a,b,c))


sinus = lambda x: +150+150*m.sin(float(x)/100)

lol = lambda x: +150+150*(m.sin(m.sin(float(x)/100)/(2*m.pi)))

#writeCode(compileCode(curve_of_function(lol, [i*5 for i in range(1500,-100,-1)])))
