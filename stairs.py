import maya.cmds as cmds
import math
import sys

SelectedObj = cmds.ls(selection=True)
Number= len(SelectedObj)

#---This part makes you select one object to use as the stair.
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
cmds.select(LocatorA)
cmds.move(-23,2.2,6)
#End temporary pieces

cmds.select(clear=True)
cmds.select('StairStep')

#---This part gets the width of the selected model in the scene's units.
selectedStair = cmds.ls( selection=True )
xmin, ymin, zmin, xmax, ymax, zmax, = cmds.xform(selectedStair, q=True, bb=True, ws=True)
StairWidth = (abs(xmin))+(abs(xmax))


#---This part gets the locations of the locators.
LocatorATranslateX = cmds.getAttr ('LocatorA.translateX')
LocatorATranslateZ = cmds.getAttr ('LocatorA.translateZ')
LocatorATranslateY = cmds.getAttr ('LocatorA.translateY')
LocatorBTranslateX = cmds.getAttr ('LocatorB.translateX')
LocatorBTranslateZ = cmds.getAttr ('LocatorB.translateZ')
LocatorBTranslateY = cmds.getAttr ('LocatorB.translateY')

#--This part gets the length of the space between LocatorA and LocatorB, and then divides it by the width of the stairs-
#and rounds it to the nearest integer. This determines the number of stairs that will be generated.
StairNumber = round(((math.sqrt(((pow((LocatorBTranslateZ-LocatorATranslateZ), 2))+(pow((LocatorBTranslateX-LocatorATranslateX), 2)))))/StairWidth))
LineLength = math.sqrt((pow((LocatorBTranslateX-LocatorATranslateX), 2)+(pow((LocatorBTranslateZ-LocatorATranslateZ),2))))

#-----------------------------------------------
    #Thinking
    #So, I need to figure out how to place the points. What I want is to place a number of points, equal to StairNumber, on the line between 
    #LocatorA and LocatorB.
    #I want the location of each point along the vector to be 0 + (StairWidth * The number of stairs that have already been placed.)
    #I want the vector to start at the locator with a lower Y value, but it's not essential.
#-----------------------------------------------
                    
Stairs = range(StairNumber)
cmds.select (clear=True)

for stair in Stairs:
    cmds.duplicate('StairStep')
    StairIteration = str(stair+1)
    cmds.select('StairStep' + StairIteration)
    DistanceToMove = stair * StairWidth
    cmds.move((LocatorATranslateX + ((DistanceToMove/LineLength)*(LocatorBTranslateX-LocatorATranslateX))), moveX=True, moveY=False, moveZ=False)
    cmds.move((LocatorATranslateY + ((DistanceToMove/LineLength)*(LocatorBTranslateY-LocatorATranslateY))), moveX=False, moveY=True, moveZ=False)
    cmds.move((LocatorATranslateZ + ((DistanceToMove/LineLength)*(LocatorBTranslateZ-LocatorATranslateZ))), moveX=False, moveY=False, moveZ=True)






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

