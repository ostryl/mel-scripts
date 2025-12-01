#THESE ARE CLASS NOTES, NOT MY CODE


#lets go
import maya.cmds as cmds
import math
import random

#citygenerator
#god im so happpy i get to do this on linux

cmds.select (all=True)
cmds.delete ()
#forin

numIterationsX = 10
numIterationsZ = 10
buildingPhaseX = 10
buildingPhaseZ = 10
streetWidthX = 2
streetWidthZ = 2
buildingBaseRandRangeMultX = 1
buildingBaseRandRangeMultZ = 1
buildingSpireRandRangeMultX = 2
buildingSpireRandRangeMultZ = 2

for iterationZ in range(numIterationsZ):
    for iterationX in range(numIterationsX):
        #define vars
        myBuildingBaseXRand = random.random()
        myBuildingBaseXRandAdjusted = buildingPhaseX - streetWidthX - (buildingBaseRandRangeMultX * myBuildingBaseXRand)
        myBuildingBaseZRand = random.random()
        myBuildingBaseZRandAdjusted = myBuildingBaseZRand + 7
        myBuildingBaseYRand = random.random()
        myBuildingBaseYRandAdjusted = myBuildingBaseYRand * 2 + 2
        myBuildingBaseYCenter = myBuildingBaseYRandAdjusted * 0.5

        myBuildingSpireXRand = random.random()
        myBuildingSpireXRandAdjusted = myBuildingSpireXRand * 1.5 + 5
        myBuildingSpireZRand = random.random()
        myBuildingSpireZRandAdjusted = myBuildingSpireZRand * 1.5 + 5
        myBuildingSpireYRand = random.random()
        myBuildingSpireYRandAdjusted = myBuildingSpireYRand * 20 + 10
        myBuildingSpireYCenter = myBuildingSpireYRandAdjusted * 0.5


        #create geo
        #mybuildingbase

        myBuildingBase = cmds.polyCube( w=3, h=1, d=3, sx=2, sy=1, sz=2, ax=[0,1,0], cuv=1, ch=True)
        #spire
        myBuildingSpire = cmds.polyCube( w=2, h=6, d=2, sx=2, sy=1, sz=2, ax=[0,1,0], cuv=2, ch=True)
        #create shaders
        myBaseShader = cmds.shadingNode('aiStandardSurface', asShader= True)
        mySpireShader = cmds.shadingNode('aiStandardSurface', asShader= True)
        #assign shaders to geo
        cmds.select(myBuildingBase)
        cmds.hyperShade(assign=myBaseShader)
        cmds.select(myBuildingSpire)
        cmds.hyperShade(assign=mySpireShader)
        #adjustments to geo
        cmds.select(myBuildingBase)
        cmds.move(iterationX * 10, myBuildingBaseYCenter, iterationZ * 10)
        cmds.select(myBuildingSpire)
        cmds.move(iterationX * 10, myBuildingSpireYCenter + iterationZ * 10)


        myRandR = random.random()
        myRandG = random.random()
        myRandB = random.random()
        cmds.setAttr(mySpireShader + '.color', myRandR, myRandG, myRandB, type="double3")
randomOperation = random.randint(1,5)
