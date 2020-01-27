import random
'''
Langton's Ant - Is a  cellular automaton program that demostrates how emergent behavior can be created from a simple rule set.
                It is a program that is like Conway Game of Life.

Rules:
At a white square, turn 90° right, flip the color of the square, move forward one unit
At a black square, turn 90° left, flip the color of the square, move forward one unit
'''
# Screen size (screenx, screeny)
screenx = 600
screeny = 400
# Size of the grid (numrows, numcols)
numrows = 30
numcols = 20
# Margin from the edges to the grid (marginx, marginy)
marginx = 40
marginy = 40
# Frames per second
fps = 4
# Number of times the ant has moved
generation = 0
# keeps the state of rather the program is running or stopped
status = 0
# antpos - grid location of the ant, antdir - holds the direction the ant is pointing
antpos = [0,0]
antdir = 0
# gets the pixel value for the start of the grid
lifex = (screenx-(marginx*2))/numrows
lifey = (screeny-(marginy*2))/numcols
# is an array that represent the state of the grid. 1 = white and 0 = red
# thus boxlist[1][1] = 0 means the box at grid col 1 and row 1 is white
boxlist = []
rowlist = []
# img will hold the sprites(images) for the ant
img0 = ''
img1 = ''
img2 = ''
img3 = ''
imgred0 = ''
imgred1 = ''
imgred2 = ''
imgred3 = ''

def setup():
    global boxlist, img0, img1, img2, img3, imgred0, imgred1, imgred2, imgred3, fps
    size(600,400)  # might have to adjust based on the number of cells
    frameRate(fps)  # can adjusted recomment values 1-10
    background(0, 0, 0)
    img0 = loadImage("ant0.png", "png")
    img1 = loadImage("ant1.png", "png")
    img2 = loadImage("ant2.png", "png")
    img3 = loadImage("ant3.png", "png")
    imgred0 = loadImage("antred0.png", "png")
    imgred1 = loadImage("antred1.png", "png")
    imgred2 = loadImage("antred2.png", "png")
    imgred3 = loadImage("antred3.png", "png")
    setupant()
    setupboard()
        
def draw():
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist,status,options
    background(0, 0, 0)
    drawlife()
    if(status == 0):
        drawant()
    drawbuttons()
    drawtext()
    
def setupboard():
    global numcols,numrows,boxlist,rowlist
    list2 = rowlist
    for l in range(numcols):
        list2 = []
        for k in range(numrows):
            list2.append(0)
        boxlist.append(list2)
        
def setupant():
    global numcols,numrows, antpos, antdir
    x = random.randint(1, numcols - 5)
    y = random.randint(1, numrows - 5)
    antdir = random.randint(0,3)
    antpos[1] = y  #.append(y)
    antpos[0] = x  #.append(x)
    
def randomlife(n):
    global lifex,lifey,numcols,numrows,marginx,marginy,boxlist
    for k in range(n):
        randx = random.randint(0,numrows-1)
        randy = random.randint(0,numcols-1)
        boxlist[randy][randx] = 1
    
def setpercent(n):
    global numrows, numcols
    t=numrows*numcols*n/100
    randomlife(t)
    
def drawlife():
    # Draws the board
    for l in range(numcols):
        for k in range(numrows):
            if(boxlist[l][k] == 1):
                fill(200,20,20)
            else:
                fill(255,255,255)
            rect(marginx+(k*lifex),marginy+(l*lifey),lifex,lifey)

def drawant():
    # Draws the ant to the screen
    global img, antdir, boxlist, generation
    generation += 1
    boxcolor = 0
    x = marginx + (antpos[0] * lifex) + 2
    y = marginy + (antpos[1] * lifey) + 2
    w = lifex-2
    h = lifey-2
    # flip the color of the ant position and change ant rotation
    #print("x - ", antpos[0])
    #print("y - ", antpos[1])
    checkantpos()
    if(boxlist[antpos[1]][antpos[0]] == 1):
        antdir -= 1
        boxlist[antpos[1]][antpos[0]] = 0
        boxcolor = 0
    else:
        antdir += 1
        boxlist[antpos[1]][antpos[0]] = 1
        boxcolor = 1
    # makesure antdir is between 0 and 3
    if(antdir > 3):
        antdir = 0
    if(antdir < 0):
        antdir = 3
    # change image to the right image based on rotation
    #print("antdir - ",antdir)
    if(antdir == 0):
        if(boxcolor == 0):
            image(img0, x, y, w, h)
        else:
            image(imgred0, x, y, w, h)
        antpos[1] -= 1
    elif(antdir == 1):
        if(boxcolor == 0):
            image(img1, x, y, w, h)
        else:
            image(imgred1, x, y, w, h)
        antpos[0] += 1
    elif(antdir == 2):
        if(boxcolor == 0):
            image(img2, x, y, w, h)
        else:
            image(imgred2, x, y, w, h)
        antpos[1] += 1
    else:
        if(boxcolor == 0):
            image(img3, x, y, w, h)
        else:
            image(imgred3, x, y, w, h)
        antpos[0] -= 1
    checkantpos()
        
def checkantpos():
    global numrows, numcols
    if(antpos[0] < 0):
        antpos[0] = numrows - 1
    if(antpos[0] > numrows - 1):
        antpos[0] = 0
    if(antpos[1] < 0):
        antpos[1] = numcols - 1
    if(antpos[1] > numcols - 1):
        antpos[1] = 0

def drawbuttons():
    # Draws Buttons to screen
    #buttons - stop/start, settings, loadfile, reset
    global screenx, screeny, numrows, numcols, marginx, marginy, options
    fill(20,200,20)
    rect(marginx,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*2/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    rect(screenx-marginx-screenx*3/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    #rect(screenx-marginx-screenx*4/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    #rect(screenx-marginx-screenx*5/10,screeny-(marginy*3/4),screenx/10,marginy/2)
    
def drawtext():
    # Draws Text to the screen
    global generation, marginx, marginy, options
    textSize(12);
    fill(200,200,200)
    text("Langton's Ant",100, marginy/1.5)
    text("Count "+str(generation), 450, marginy/1.5) 
    text("Restart",marginx+10,screeny-(marginy*3/4)+15)
    if(status==0):
        text("Stop",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    else:
        text("Start",screenx-marginx-screenx/10+15,screeny-(marginy*3/4)+15)
    text("Random",screenx-marginx-screenx*2/10+8,screeny-(marginy*3/4)+15)
    text("Clear",screenx-marginx-screenx*3/10+15,screeny-(marginy*3/4)+15)

def boardclick(x,y):
    global numcols,numrows,marginx,marginy,boxlist,lifex,lifey
    for l in range(numcols):
        for k in range(numrows):
            if(x>marginx+(k*lifex) and x<marginx+(k*lifex)+lifex and y>marginy+(l*lifey) and y<marginy+(l*lifey)+lifey):
                if(boxlist[l][k]==1):
                    boxlist[l][k] = 0
                else:
                    boxlist[l][k] = 1
                    
def mousePressed():
    global numrows, numcols, marginx, marginy, screenx, screeny, boxlist, generation, status
    x=mouseX
    y=mouseY
    if(x>screenx-marginx-screenx*3/10 and x<screenx-marginx-screenx*3/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Clear Button
        generation = 0
        status = 1
        boxlist=[]
        setupboard()
        return
    if(x>screenx-marginx-screenx*2/10 and x<screenx-marginx-screenx*2/10+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Random Button
        generation = 0
        status = 0
        boxlist=[]
        setupant()
        setupboard()
        setpercent(20)
        return
    if(x>marginx and x<marginx+screenx/10 and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Restart
        generation = 0
        status = 0
        boxlist=[]
        setupant()
        setupboard()
        return
    if(x>screenx-marginx-screenx/10 and x<screenx-marginx and y>screeny-(marginy*3/4) and y<screeny-(marginy*3/4)+marginy/2):
        # Start/Stop button
        if(status==0):
            status = 1
        else:
            status = 0
        return
    boardclick(x,y)
