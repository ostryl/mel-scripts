import maya.cmds as cmds
import math
import random
#I want to make code that generates stairs based on the location of two locators, which the user can control in the viewport
#The user should be able to change the height/size of the stairs and the code should accomodate that.
#How is this better than MASH, though? Seems like a waste of time but meh, screw it
#Would be cool if it had a GUI
#Clear selection
cmds.select (clear=1)
#Create locators
LocatorA = cmds.spaceLocator (name="LocatorA")
LocatorB = cmds.spaceLocator (name="LocatorB")
#Maybe I could iterate down the list of locators until the largest two numbers (eg. locator8 and locator9) and select those?
#There's a name flag. Wow. RTFM, right? How do I get the script to pull custom geometry? 
#Seriously, is this even worth it when MASH exists?
#The position X of the stairs should be the width of the distance between. The stairs should rotate to face the direction of the lower locator
#There should be a way to add some random tilting to make the stairs look old.

LocatorATranslateX = cmds.getAttr ('LocatorA.translateX')
LocatorATranslateZ = cmds.getAttr ('LocatorA.translateZ')
LocatorATranslateY = cmds.getAttr ('LocatorA.translateY')
LocatorBTranslateX = cmds.getAttr ('LocatorB.translateX')
LocatorBTranslateZ = cmds.getAttr ('LocatorB.translateZ')
LocatorBTranslateY = cmds.getAttr ('LocatorB.translateY')
StairWidth = 0.5

StairNumber = round(((math.sqrt(((pow((LocatorBTranslateZ-LocatorATranslateZ), 2))+(pow((LocatorBTranslateX-LocatorATranslateX), 2)))))/StairWidth))
print(StairNumber)
Stairs = range(StairNumber)
#If LocatorATranslateX > LocatorBTranslateX, StairTranslateX = LocatorATranslateX - (Stair width * the # current number of stairs)
#Elseif LocatorStairTranslateX < LocatorTranslateX, StairTranslateX = LocatorATranslateX + (Stair width * the # current number of stairs)
#Else 

for stair in Stairs:
    #Define vars
    print("for")
    #Create geo

#Testing
cmds.select(LocatorA)
cmds.move(5,5,5)

#StairRotation
#StairRangeX = The difference between LocatorATranslateX and LocatorBTranslateX
#The number of stairs should be StairRangeX/StairWidth, rounded to the nearest integer

#The translation can be negative. It needs to be the difference between them. 

#Then, the
#The position Y of the stairs should be 

#Transform geo

