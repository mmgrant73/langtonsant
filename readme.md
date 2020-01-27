
# Langton's Ant:

### What is it?
Langton's Ant is a cellular automaton program (a discrete model studied in computer science) that demonstrates how emergent behavior can be 
created from a simple rule set.  Cellular automaton consists of a regular grid of cells, each in one of a finite number of states, 
such as on and off (ie. alive or dead).  How these cells evolve off time is define by a simple rule set.  It was invented by Chris Langton in 1986

Rule Set:
1. At a white square, turn 90° right, flip the color of the square, move forward one unit
2. At a red square, turn 90° left, flip the color of the square, move forward one unit

![Alt text](https://github.com/mmgrant73/langtonsant/blob/master/life.png?raw=true "Image-RevealBox")

[For more infomation:](https://en.wikipedia.org/wiki/Langton%27s_ant) 

### Programming:
This was written using the Processing Programming Language in Python Mode.  Processing is an open source framework that lets a user write programs 
with a visual context using javascript, java or python.  Processing has promoted software literacy, particularly within the visual arts, and 
visual literacy within technology.  And personally I think it is a great for people just getting into programming. 
[For more infomation:](https://processing.org/) 

### How to run it?
To use this program, just download the Processing IDE at https://processing.org/download/ , clone this respository.  Install and open the IDE and open 
the langtonsant.pyde file.

### How to use it?
When the program begins the ant will be place randomly on a clear grid and it will start the process defined by the ruleset.  The grid is suppose to
be infinity in size which is not possible, thus the only deviation from the ruleset is the edge cases.  In my version, when the ant goes off the 
grid, it will reappear on the opposite side of the grid.

Buttons:
1. Start/Stop: allows you to start or pause the program
2. Restart: Will start the program over from the start, clearing the grid( turning all boxes to white) and randomly place the ant in the grid
3. Random: Will randomly set up the grid to either red or white squares.  After which it will randomly place the ant in the grid
4. Clear: Will clear the grid to all white boxes but keep the ant at its current location

Customization:
You can set the gridsize if you choose.  At the top of the program there are two variables numrows, numcols that determine its size.  They are set by 
default to 20 X 30.  You can also set the screen size which is defined by screenx and screeny variables at the top of the program.  By default the screen
is set to 600 X 400.  You can also adjust the framerate, which will affect the speed of the program.  By default it is set to 4fps

Note: If you like this type of program, I have a project Conways' Game of Life which is another cellular automation program.
