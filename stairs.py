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
cmds.move(5,5,5)

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

Stairs = range(StairNumber)
#If LocatorATranslateX > LocatorBTranslateX, StairTranslateX = LocatorATranslateX - (Stair width * the # current number of stairs)
#Elseif LocatorStairTranslateX < LocatorTranslateX, StairTranslateX = LocatorATranslateX + (Stair width * the # current number of stairs)
#Else 
cmds.select (clear=True)
for stair in Stairs:
    #Define vars
    #--Create geo. We need a way to use the selected object as the stair.
    cmds.duplicate('StairStep')
    StairIteration = str(stair+1)
    cmds.select('StairStep' + StairIteration)
    cmds.move(stair * StairWidth, stair * StairWidth, stair * StairWidth)
    cmds.select (clear=True)
    print(stair)
#Testing

#StairRotation
#StairRangeX = The difference between LocatorATranslateX and LocatorBTranslateX
#The number of stairs should be StairRangeX/StairWidth, rounded to the nearest integer

#The translation can be negative. It needs to be the difference between them. 

#Then, the
#The position Y of the stairs should be 

#Transform geo

