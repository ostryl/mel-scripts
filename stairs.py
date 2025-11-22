import maya.cmds as cmds
import math
import sys
#--I want to make code that generates stairs based on the location of two locators, which the user can control in the viewport
#--The user should be able to change the height/size of the stairs and the code should accomodate that.

#---This section gets the number of selected objects, and throws an error if more or less than one object is selected.
SelectedObj = cmds.ls(selection=True)
Number= len(SelectedObj)

if Number == 0:
    sys.exit('You need to select an object!')
elif Number > 1:
    sys.exit('You have multiple objects selected, please only select one!')
else:
    print('Stair building in progress...')
    cmds.rename (SelectedObj, 'StairStep')

#---This part creates the locators.
LocatorA = cmds.spaceLocator (name='LocatorA')
LocatorB = cmds.spaceLocator (name='LocatorB')

#These pieces are temporary and should be removed. I need to replace StairWidth with the width of the selected object, and cmds.move will need to be based on the locator instead.
StairWidth = 1
cmds.select(LocatorA)
cmds.move(-23,2.2,6)

#The position X of the stairs should be the width of the distance between. The stairs should rotate to face the direction of the lower locator
#There should be a way to add some random tilting to make the stairs look old.

LocatorATranslateX = cmds.getAttr ('LocatorA.translateX')
LocatorATranslateZ = cmds.getAttr ('LocatorA.translateZ')
LocatorATranslateY = cmds.getAttr ('LocatorA.translateY')
LocatorBTranslateX = cmds.getAttr ('LocatorB.translateX')
LocatorBTranslateZ = cmds.getAttr ('LocatorB.translateZ')
LocatorBTranslateY = cmds.getAttr ('LocatorB.translateY')

#--This part gets the length of the space between LocatorA and LocatorB, and then divides it by the width of the stairs-
#and rounds it to the nearest integer. This determines the number of stairs that will be generated.
StairNumber = round(((math.sqrt(((pow((LocatorBTranslateZ-LocatorATranslateZ), 2))+(pow((LocatorBTranslateX-LocatorATranslateX), 2)))))/StairWidth))


UnitVector = ()

#-----------------------------------------------
    #Thinking
    #So, I need to figure out how to place the points. What I want is to place a number of points, equal to StairNumber, on the line between 
    #LocatorA and LocatorB.
    #I want the location of each point along the vector to be 0 + (StairWidth * The number of stairs that have already been placed.)
    #I want the vector to start at the locator with a lower Y value, but it's not essential.

#-----------------------------------------------

#How do I place a point at a certain distance on a line?

#LineVector = (LocatorBTranslateX-LocatorATranslateX, LocatorBTranslateY-LocatorATranslateY, LocatorBTranslateZ-LocatorATranslateZ)
#LineMagnitude = abs(math.sqrt((pow((LocatorBTranslateX-LocatorATranslateX), 2)+(pow((LocatorBTranslateZ-LocatorATranslateZ),2)))))
#NormalDirectionVector = LineVector / LineMagnitude
#StartY = min(LocatorATranslateY, LocatorBTranslateY)

                    
Stairs = range(StairNumber)
#If LocatorATranslateX > LocatorBTranslateX, StairTranslateX = LocatorATranslateX - (Stair width * the # current number of stairs)
#Elseif LocatorStairTranslateX < LocatorTranslateX, StairTranslateX = LocatorATranslateX + (Stair width * the # current number of stairs)
#Else 

#If LocatorATranslateZ > 


cmds.select (clear=True)
for stair in Stairs:
    #Define vars
    #--Create geo. We need a way to use the selected object as the stair.
    cmds.duplicate('StairStep')
    StairIteration = str(stair+1)
    cmds.select('StairStep' + StairIteration)
    Slope = (LocatorATranslateZ - LocatorBTranslateZ)-(LocatorATranslateX-LocatorBTranslateX)
    #cmds.move(LocatorATranslateX + stair * ((LocatorBTranslateX-LocatorATranslateX)/(StairNumber-1)), moveX=True, moveY=False, moveZ=False)
    #cmds.move(LocatorATranslateY + StartY * ((LocatorBTranslateY-LocatorATranslateY)/(StairNumber-1)), moveX=False, moveY=True, moveZ=False)
    #cmds.move(LocatorATranslateZ + stair * ((LocatorBTranslateZ-LocatorATranslateZ)/(StairNumber-1)), moveX=False, moveY=False, moveZ=True)
    #if LocatorATranslateX > LocatorBTranslateX :

        #cmds.move((LocatorATranslateX + (StairWidth * stair)), moveX=True, moveY=False, moveZ=False)
        #so in this case -23 + (1 * 0)
        #so it ends up being -23
        #cmds.move
        #but we want it to be that stair 0 is at 0 and stair 23 is at -23
        #ugh wtf
        #I want the stairs to be placed at even intervals on a straight line from one point to another, from a central point

        #the translation of the stair should be like, 

        #cmds.move((Slope * stair), moveX=True, moveY=False, moveZ=False)
    #else :
        #cmds.move((LocatorATranslateX + (StairWidth * stair)), moveX=True, moveY=False, moveZ=False)
        #cmds.move((Slope * stair), moveX=True, moveY=False, moveZ=False)
   
        #let's say outerpoint is at -20. i want the stairs, starting at 0, 



        #6 + (1*1)
    #--Gotta figure it out for the others now




    #if LocatorATranslateZ > LocatorBTranslateZ :
        #cmds.move((LocatorATranslateZ + (StairWidth * stair)), moveX=False, moveY=False, moveZ=True)


    #6 = 6 + (1 * 1)
    #0 = 6 + (1 * 24)

    # I want the translateZ of the stairs to equal 

    #we need translatez to equal 6 for stair one and zero for stair 24


    #else :
        #cmds.move((LocatorATranslateZ + (StairWidth * stair)), moveX=False, moveY=False, moveZ=True)
    #cmds.move(stair * StairWidth, stair * StairWidth, stair * StairWidth)
    #This line needs to be fixed
    #It gets worse as we go towards 24 and the number gets bigger
    #when locatorAtranslateZ= -23, we need 1 * 24


#StairStep 1 is great but the rest are way off






cmds.select (clear=True)
#Testing

#StairRotation
#StairRangeX = The difference between LocatorATranslateX and LocatorBTranslateX
#The number of stairs should be StairRangeX/StairWidth, rounded to the nearest integer

#The translation can be negative. It needs to be the difference between them. 

#Then, the
#The position Y of the stairs should be 

#Transform geo

