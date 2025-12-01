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
cmds.select(all=True)
ThingsInScene = cmds.ls(selection=True)
if 'LocatorA' not in ThingsInScene:
    LocatorA = cmds.spaceLocator (name='LocatorA')
if 'LocatorB' not in ThingsInScene:
    LocatorB = cmds.spaceLocator (name='LocatorB')

cmds.select(clear=True)
cmds.select('StairStep')

#---This part gets the width of the selected model in the scene's units.
selectedStair = cmds.ls( selection=True )
xmin, ymin, zmin, xmax, ymax, zmax, = cmds.xform(selectedStair, q=True, bb=True, ws=True)
StairWidth = (abs(xmin))+(abs(xmax))
StairHeight = (abs(ymin))+(abs(ymax))


#---This part gets the locations of the locators.
LocatorATranslateX = cmds.getAttr ('LocatorA.translateX')
LocatorATranslateZ = cmds.getAttr ('LocatorA.translateZ')
LocatorATranslateY = cmds.getAttr ('LocatorA.translateY')
LocatorBTranslateX = cmds.getAttr ('LocatorB.translateX')
LocatorBTranslateZ = cmds.getAttr ('LocatorB.translateZ')
LocatorBTranslateY = cmds.getAttr ('LocatorB.translateY')

#--This part gets the length of the space between LocatorA and LocatorB, and then divides it by the width of the stairs-
#--and rounds it to the nearest integer. This determines the number of stairs that will be generated.
StairNumber = round(((math.sqrt(((pow((LocatorBTranslateZ-LocatorATranslateZ), 2))+(pow((LocatorBTranslateX-LocatorATranslateX), 2)))))/StairWidth))
LineLength = math.sqrt((pow((LocatorBTranslateX-LocatorATranslateX), 2)+(pow((LocatorBTranslateZ-LocatorATranslateZ),2))))
                  
Stairs = range(StairNumber)
cmds.select (clear=True)

for stair in Stairs:
    cmds.duplicate('StairStep')
    StairIteration = str(stair+1)
    cmds.select('StairStep' + StairIteration)
    DistanceToMove = stair * StairWidth
    DistanceToMoveUp = stair * (StairHeight * 2)
    cmds.move((LocatorATranslateX + ((DistanceToMove/LineLength)*(LocatorBTranslateX-LocatorATranslateX))), moveX=True, moveY=False, moveZ=False)
    cmds.move((LocatorATranslateY + ((DistanceToMoveUp/LineLength)*(LocatorBTranslateY-LocatorATranslateY))), moveX=False, moveY=True, moveZ=False)
    cmds.move((LocatorATranslateZ + ((DistanceToMove/LineLength)*(LocatorBTranslateZ-LocatorATranslateZ))), moveX=False, moveY=False, moveZ=True)

cmds.select (clear=True)



#Okay and next, we need a GUI and some procedures
#We need to be able to interact with the locators. How do I make that happen?
#Let's say we run the script. Now we want to move

#Maybe we could check if LocatorA and LocatorB exist, and if they do don't create them. Delete all StairStep duplicates (not the OG mesh)
#then run the script again from a button? 
#Problem: The script uses existing stairs if it's been used once and hasn't been deleted.
#Maybe I could fix this by merging and renaming the stair groups?
#