import maya.cmds as cmds
import math
import sys

OriginalObj = cmds.ls(selection=True)
print(OriginalObj)
def SelectAll():
    cmds.select(allDagObjects=True)

def ClearSelection():
    cmds.select(clear=True)

def SelectBaseStair():
    cmds.select('StairStep')


SelectAll()
SelectedObj = cmds.ls(selection=True)
Number= len(OriginalObj)


if 'StairStep' not in SelectedObj:
    if Number == 0:
        sys.exit('You need to create or select an object!')
    elif Number > 1:
        sys.exit('You have multiple objects selected and none of them are named StairStep, please select your target object or name it StairStep!')
    else:
        print('Stair building in progress. Hint: Move your locators!')
        cmds.rename (OriginalObj, 'StairStep')

#---This part creates the locators.
SelectAll()
ThingsInScene = cmds.ls(selection=True)
if 'LocatorA' not in ThingsInScene:
    LocatorA = cmds.spaceLocator (name='LocatorA')
if 'LocatorB' not in ThingsInScene:
    LocatorB = cmds.spaceLocator (name='LocatorB')


ClearSelection()
SelectBaseStair()

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

if (LocatorBTranslateX-LocatorATranslateX) != 0 and (LocatorBTranslateZ-LocatorATranslateZ) != 0 :
    Gradient = (LocatorBTranslateX-LocatorATranslateX)/(LocatorBTranslateZ-LocatorATranslateZ)
    StairRotationRadians = math.atan(Gradient)
    StairRotationDegrees = (math.degrees(StairRotationRadians)) + 90

Stairs = range(StairNumber)
ClearSelection()

def MakeStairs():
    for stair in Stairs:
        cmds.duplicate('StairStep')
        StairIteration = str(stair+1)
        cmds.select('StairStep' + StairIteration)
        cmds.rename('StairStep' + StairIteration)
        DistanceToMove = stair * StairWidth
        DistanceToMoveUp = stair * (StairHeight)
        cmds.move((LocatorATranslateX + ((DistanceToMove/LineLength)*(LocatorBTranslateX-LocatorATranslateX))), moveX=True, moveY=False, moveZ=False)
        cmds.move((LocatorATranslateY + ((DistanceToMoveUp/LineLength)*(LocatorBTranslateY-LocatorATranslateY))), moveX=False, moveY=True, moveZ=False)
        cmds.move((LocatorATranslateZ + ((DistanceToMove/LineLength)*(LocatorBTranslateZ-LocatorATranslateZ))), moveX=False, moveY=False, moveZ=True)
        if (LocatorBTranslateX-LocatorATranslateX) != 0 and (LocatorBTranslateZ-LocatorATranslateZ) != 0 :
            Rotate = str(StairRotationDegrees) + 'deg'
            cmds.rotate(0, Rotate, 0,)

MakeStairs()
ClearSelection()
SelectAll()

NeedToRename = cmds.ls(selection=True)

if 'StairStep' in NeedToRename:
    SelectBaseStair()
    cmds.rename('JustATempStair')
    if LocatorATranslateX == 0 and LocatorATranslateY == 0 and LocatorATranslateZ == 0 and LocatorBTranslateX == 0 and LocatorBTranslateY == 0 and LocatorBTranslateZ == 0:
        cmds.select('JustATempStair')
        cmds.rename(OriginalObj)
    else:
        cmds.select ("StairStep*")
        cmds.polyUnite (centerPivot=True)
        cmds.delete(ch=True)
        cmds.select('JustATempStair')
        cmds.rename(OriginalObj)
ClearSelection()




#I want the stairs to add an _# onto the end if the for loop has already been run. 

#Okay and next, we need a GUI and some procedures
#We need to be able to interact with the locators. How do I make that happen?
#Let's say we run the script. Now we want to move

#Maybe we could check if LocatorA and LocatorB exist, and if they do don't create them. Delete all StairStep duplicates (not the OG mesh)
#then run the script again from a button? 
#Problem: The script uses existing stairs if it's been used once and hasn't been deleted.
#Maybe I could fix this by merging and renaming the stair groups?
#