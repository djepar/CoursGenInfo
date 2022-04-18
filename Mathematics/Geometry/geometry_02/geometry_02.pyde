#https://processing.org/reference/

t = 0

def setup():
    size(600,600)
    rectMode(CENTER)

def draw():
    global t
    background(255)
    
    #first 2 parameters : where the center started
    # last 2 : width and height
    #rect(20,40,50,30)
    
    #to move the origin (0,0) to the center of the canvas
    translate(width/2, height/2)
    rotate(radians(t))
        
    for i in range(12):
        pushMatrix() #save this orientation
        translate(200,0)
#        rotate(radians(t)) slower than 5*t
        rotate(radians(5*t))
        rect(0,0,50,50)
        popMatrix() #return to the saved orientation
        rotate(radians(360/12))
    t+=1
        
        
